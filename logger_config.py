"""日志配置和管理模块"""

import logging
from datetime import datetime, timedelta
from pathlib import Path


def cleanup_old_logs(log_file='friday.log', days=7):
    """
    清理超过指定天数的日志文件
    
    Args:
        log_file: 日志文件路径
        days: 日志保留天数，默认 7 天
    """
    log_path = Path(log_file)
    
    if not log_path.exists():
        return
    
    # 检查文件修改时间
    file_mtime = datetime.fromtimestamp(log_path.stat().st_mtime)
    age_days = (datetime.now() - file_mtime).days
    
    if age_days >= days:
        # 备份旧日志
        backup_name = f"friday_{file_mtime.strftime('%Y%m%d')}.log"
        backup_path = log_path.parent / 'logs_archive' / backup_name
        backup_path.parent.mkdir(exist_ok=True)
        
        # 移动到归档目录
        log_path.rename(backup_path)
        print(f"日志已归档: {backup_name} (文件已存在 {age_days} 天)")
    
    # 清理归档目录中超过 4 周的日志
    archive_dir = log_path.parent / 'logs_archive'
    if archive_dir.exists():
        cutoff_date = datetime.now() - timedelta(days=28)  # 4 周
        for old_log in archive_dir.glob('friday_*.log'):
            if datetime.fromtimestamp(old_log.stat().st_mtime) < cutoff_date:
                old_log.unlink()
                print(f"已删除旧日志: {old_log.name}")


def setup_logging(log_file='friday.log', level=logging.INFO):
    """
    配置日志系统
    
    Args:
        log_file: 日志文件路径
        level: 日志级别
    
    Returns:
        logger: 配置好的日志记录器
    """
    # 启动时清理旧日志
    cleanup_old_logs(log_file)
    
    # 配置基础日志
    logging.basicConfig(
        level=level,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file, encoding='utf-8')
        ]
    )
    
    # 获取主日志记录器
    logger = logging.getLogger(__name__)
    
    # 设置第三方库的日志级别为 WARNING，避免过多输出
    logging.getLogger('agentscope').setLevel(logging.WARNING)
    logging.getLogger('openai').setLevel(logging.WARNING)
    logging.getLogger('httpx').setLevel(logging.WARNING)
    
    return logger

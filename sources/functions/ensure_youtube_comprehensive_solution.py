from sources.functions.ensure_seconds_measured import ensure_seconds_measured
import logging
from sources.objects.pk_local_test_activate import LTA
from pathlib import Path
import os
import json
import time
import subprocess
from datetime import datetime, timedelta
from typing import List, Dict, Any, Optional, Tuple


class ComprehensiveYouTubeSolution:
    """
    YouTube 연령 제한 동영상 다운로드 문제를 해결하기 위한 종합 솔루션
    방안 1, 2, 3, 4를 모두 자동으로 실행
    """
    
    def __init__(self):
        self.solution_results = {}
        self.current_step = 0
        self.total_steps = 4
        
        # 해결 방안 정의
        self.solutions = {
            'solution_1': {
                'name': 'Windows 환경에서 직접 실행',
                'description': 'Windows PowerShell에서 직접 실행하여 환경 문제 해결',
                'function': self._execute_solution_1,
                'enabled': True
            },
            'solution_2': {
                'name': '쿠키 파일 수동 갱신',
                'description': 'Chrome에서 새로운 쿠키를 내보내고 적용',
                'function': self._execute_solution_2,
                'enabled': True
            },
            'solution_3': {
                'name': '고급 옵션으로 재시도',
                'description': '향상된 User-Agent, 헤더, 재시도 옵션 사용',
                'function': self._execute_solution_3,
                'enabled': True
            },
            'solution_4': {
                'name': 'yt-dlp 최신 버전으로 업데이트',
                'description': 'yt-dlp를 최신 버전으로 업데이트하여 호환성 문제 해결',
                'function': self._execute_solution_4,
                'enabled': True
            }
        }
    
    def execute_all_solutions(self, test_url: str = None) -> Dict[str, Any]:
        """
        모든 해결 방안을 순차적으로 실행
        
        Args:
            test_url: 테스트할 YouTube URL (None이면 기본 URL 사용)
            
        Returns:
            Dict[str, Any]: 실행 결과 요약
        """
        if test_url is None:
            test_url = "https://www.youtube.com/watch?v=6jQOQQA7-eA"  # 연령 제한 동영상 테스트용
        
        logging.debug("YouTube 연령 제한 동영상 다운로드 종합 솔루션 시작")
        logging.debug(f"테스트 URL: {test_url}")
        logging.debug(f"총 {self.total_steps}개 해결 방안 실행 예정")
        
        # 각 해결 방안 실행
        for solution_key, solution_info in self.solutions.items():
            if not solution_info['enabled']:
                continue
            
            self.current_step += 1
            logging.debug(f"\n{'='*60}")
            logging.debug(f"[{self.current_step}/{self.total_steps}] {solution_info['name']}")
            logging.debug(f"{solution_info['description']}")
            logging.debug(f"{'='*60}")
            
            try:
                # 해결 방안 실행
                start_time = time.time()
                result = solution_info['function'](test_url)
                execution_time = time.time() - start_time
                
                # 결과 기록
                self.solution_results[solution_key] = {
                    'success': result['success'],
                    'message': result['message'],
                    'execution_time': execution_time,
                    'timestamp': datetime.now().isoformat(),
                    'details': result.get('details', {})
                }
                
                if result['success']:
                    logging.debug(f"{solution_info['name']} 성공!")
                    logging.debug(f"{result['message']}")
                    
                    # 성공한 경우 다음 단계로 진행할지 확인
                    if self._should_continue_after_success():
                        logging.debug("다음 해결 방안도 실행하여 완벽한 해결을 확인합니다.")
                    else:
                        logging.debug("해결 완료! 추가 실행을 중단합니다.")
                        break
                else:
                    logging.debug(f"{solution_info['name']} 실패")
                    logging.debug(f"{result['message']}")
                    
                    # 실패한 경우 다음 방안으로 진행
                    logging.debug("다음 해결 방안으로 진행합니다.")
                
            except Exception as e:
                logging.debug(f"{solution_info['name']} 실행 중 오류 발생: {str(e)}")
                self.solution_results[solution_key] = {
                    'success': False,
                    'message': f"실행 중 오류: {str(e)}",
                    'execution_time': 0,
                    'timestamp': datetime.now().isoformat(),
                    'details': {'error': str(e)}
                }
        
        # 최종 결과 요약
        return self._generate_final_summary()
    
    def _execute_solution_1(self, test_url: str) -> Dict[str, Any]:
        """방안 1: Windows 환경에서 직접 실행"""
        try:
            logging.debug("Windows 환경에서 직접 실행 시도 중...")
            
            # Windows PowerShell 명령 구성
            ps_commands = [
                f"cd 'C:\\Users\\pk_system_security_literal\\Downloads\\task_orchestrator_cli'",
                "python -m resources.functions.ensure_youtube_videos_downloaded_v3_advanced"
            ]
            
            ps_script = "; ".join(ps_commands)
            
            # PowerShell 실행
            cmd = ["powershell.exe", "-Command", ps_script]
            
            logging.debug(f"실행 명령: {' '.join(cmd)}")
            
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=300  # 5분 타임아웃
            )
            
            if result.returncode == 0:
                return {
                    'success': True,
                    'message': 'Windows 환경에서 직접 실행 성공',
                    'details': {
                        'stdout': result.stdout,
                        'stderr': result.stderr
                    }
                }
            else:
                return {
                    'success': False,
                    'message': f'Windows 실행 실패 (코드: {result.returncode})',
                    'details': {
                        'stdout': result.stdout,
                        'stderr': result.stderr
                    }
                }
                
        except subprocess.TimeoutExpired:
            return {
                'success': False,
                'message': 'Windows 실행 시간 초과 (5분)',
                'details': {'error': 'timeout'}
            }
        except Exception as e:
            return {
                'success': False,
                'message': f'Windows 실행 중 오류: {str(e)}',
                'details': {'error': str(e)}
            }
    
    def _execute_solution_2(self, test_url: str) -> Dict[str, Any]:
        """방안 2: 쿠키 파일 수동 갱신"""
        try:
            logging.debug("쿠키 파일 수동 갱신 시도 중...")
            
            # n. 기존 쿠키 백업
            from sources.objects.task_orchestrator_cli_directories import D_TASK_ORCHESTRATOR_CLI_SENSITIVE
            cookie_dir = D_TASK_ORCHESTRATOR_CLI_SENSITIVE
            
            if cookie_dir.exists():
                # 기존 쿠키 파일들 백업
                backup_files = []
                for cookie_file in cookie_dir.glob("chrome_youtube_cookies*.txt"):
                    if cookie_file.exists():
                        backup_name = f"{cookie_file.stem}_backup_{int(time.time())}.txt"
                        backup_path = cookie_dir / backup_name
                        cookie_file.rename(backup_path)
                        backup_files.append(backup_name)
                        logging.debug(f"쿠키 백업: {backup_name}")
                
                if backup_files:
                    logging.debug(f"{len(backup_files)}개 쿠키 파일 백업 완료")
            
            # n. 새로운 쿠키 생성 시도
            cookie_creation_success = False
            
            # 방법 1: 기존 쿠키 저장 함수 사용
            try:
                from sources.functions.save_chrome_youtube_cookies_to_f import save_chrome_youtube_cookies_to_f
                if save_chrome_youtube_cookies_to_f():
                    cookie_creation_success = True
                    logging.debug("기존 쿠키 저장 함수로 새 쿠키 생성 성공")
            except Exception as e:
                logging.debug(f"️ 기존 쿠키 저장 함수 실패: {e}")
            
            # 방법 2: yt-dlp 쿠키 추출 시도
            if not cookie_creation_success:
                try:
                    from sources.functions.ensure_youtube_cookies_created_v2 import ensure_youtube_cookies_created_v2
                    if ensure_youtube_cookies_created_v2(force_refresh=True):
                        cookie_creation_success = True
                        logging.debug("yt-dlp 쿠키 추출로 새 쿠키 생성 성공")
                except Exception as e:
                    logging.debug(f"️ yt-dlp 쿠키 추출 실패: {e}")
            
            # n. 쿠키 유효성 검증
            if cookie_creation_success:
                cookie_file = cookie_dir / "chrome_youtube_cookies.txt"
                if cookie_file.exists() and cookie_file.stat().st_size > 0:
                    # 간단한 쿠키 유효성 테스트
                    if self._test_cookie_validity(cookie_file):
                        return {
                            'success': True,
                            'message': '새로운 쿠키 파일 생성 및 유효성 검증 성공',
                            'details': {
                                'cookie_file': str(cookie_file),
                                'file_size': cookie_file.stat().st_size,
                                'backup_files': backup_files
                            }
                        }
                    else:
                        return {
                            'success': False,
                            'message': '쿠키 파일은 생성되었지만 유효성 검증 실패',
                            'details': {
                                'cookie_file': str(cookie_file),
                                'backup_files': backup_files
                            }
                        }
                else:
                    return {
                        'success': False,
                        'message': '쿠키 파일 생성 실패',
                        'details': {'backup_files': backup_files}
                    }
            else:
                return {
                    'success': False,
                    'message': '모든 쿠키 생성 방법 실패',
                    'details': {'backup_files': backup_files}
                }
                
        except Exception as e:
            return {
                'success': False,
                'message': f'쿠키 갱신 중 오류: {str(e)}',
                'details': {'error': str(e)}
            }
    
    def _execute_solution_3(self, test_url: str) -> Dict[str, Any]:
        """방안 3: 고급 옵션으로 재시도"""
        try:
            logging.debug("고급 옵션으로 다운로드 재시도 중...")
            
            # 고급 다운로드 시스템 실행
            try:
                from sources.functions.ensure_youtube_videos_downloaded_v3_advanced import ensure_youtube_videos_downloaded_v3_advanced
                
                # LTA 모드 임시 비활성화 (실제 실행을 위해)
                original_lta = None
                try:
                    from sources.objects.pk_local_test_activate import LTA
                    original_lta = LTA
                    # LTA를 False로 설정하여 실제 실행
                    import resources.objects.pk_local_test_activate
                    resources.objects.pk_local_test_activate.LTA = False
                except:
                    pass
                
                # 고급 다운로드 실행
                success = ensure_youtube_videos_downloaded_v3_advanced()
                
                # LTA 원래 값으로 복원
                if original_lta is not None:
                    resources.objects.pk_local_test_activate.LTA = original_lta
                
                if success:
                    return {
                        'success': True,
                        'message': '고급 옵션으로 다운로드 성공',
                        'details': {'method': 'v3_advanced'}
                    }
                else:
                    return {
                        'success': False,
                        'message': '고급 옵션으로 다운로드 실패',
                        'details': {'method': 'v3_advanced'}
                    }
                    
            except ImportError:
                return {
                    'success': False,
                    'message': '고급 다운로드 시스템을 찾을 수 없음',
                    'details': {'error': 'ImportError'}
                }
            except Exception as e:
                return {
                    'success': False,
                    'message': f'고급 다운로드 실행 중 오류: {str(e)}',
                    'details': {'error': str(e)}
                }
                
        except Exception as e:
            return {
                'success': False,
                'message': f'고급 옵션 실행 중 오류: {str(e)}',
                'details': {'error': str(e)}
            }
    
    def _execute_solution_4(self, test_url: str) -> Dict[str, Any]:
        """방안 4: yt-dlp 최신 버전으로 업데이트"""
        try:
            logging.debug("yt-dlp 최신 버전으로 업데이트 시도 중...")
            
            # 현재 yt-dlp 버전 확인
            current_version = self._get_yt_dlp_version()
            logging.debug(f"현재 yt-dlp 버전: {current_version}")
            
            # 업데이트 시도
            update_success = False
            
            # 방법 1: uv를 사용한 업데이트
            try:
                logging.debug("uv를 사용한 yt-dlp 업데이트 시도...")
                
                cmd = ["uv", "add", "yt-dlp", "--upgrade"]
                result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
                
                if result.returncode == 0:
                    update_success = True
                    logging.debug("uv를 사용한 yt-dlp 업데이트 성공")
                else:
                    logging.debug(f"️ uv 업데이트 실패: {result.stderr}")
                    
            except Exception as e:
                logging.debug(f"️ uv 업데이트 중 오류: {e}")
            
            # 방법 2: pip를 사용한 업데이트
            if not update_success:
                try:
                    logging.debug("pip를 사용한 yt-dlp 업데이트 시도...")
                    
                    cmd = ["pip", "install", "--upgrade", "yt-dlp"]
                    result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
                    
                    if result.returncode == 0:
                        update_success = True
                        logging.debug("pip를 사용한 yt-dlp 업데이트 성공")
                    else:
                        logging.debug(f"️ pip 업데이트 실패: {result.stderr}")
                        
                except Exception as e:
                    logging.debug(f"️ pip 업데이트 중 오류: {e}")
            
            # 업데이트 후 버전 확인
            if update_success:
                new_version = self._get_yt_dlp_version()
                logging.debug(f"업데이트 후 yt-dlp 버전: {new_version}")
                
                if new_version != current_version:
                    return {
                        'success': True,
                        'message': f'yt-dlp 업데이트 성공: {current_version} → {new_version}',
                        'details': {
                            'old_version': current_version,
                            'new_version': new_version
                        }
                    }
                else:
                    return {
                        'success': False,
                        'message': 'yt-dlp 업데이트 후에도 버전이 동일함',
                        'details': {
                            'old_version': current_version,
                            'new_version': new_version
                        }
                    }
            else:
                return {
                    'success': False,
                    'message': '모든 yt-dlp 업데이트 방법 실패',
                    'details': {'current_version': current_version}
                }
                
        except Exception as e:
            return {
                'success': False,
                'message': f'yt-dlp 업데이트 중 오류: {str(e)}',
                'details': {'error': str(e)}
            }
    
    def _test_cookie_validity(self, cookie_file: Path) -> bool:
        """쿠키 파일 유효성 간단 테스트"""
        try:
            with open(cookie_file, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            
            # 최소한의 쿠키 데이터 확인
            cookie_lines = [line for line in lines if line.strip() and not line.startswith('#')]
            
            if len(cookie_lines) < 3:
                return False
            
            # YouTube 도메인 쿠키 확인
            youtube_cookies = [line for line in cookie_lines if '.youtube.com' in line]
            
            return len(youtube_cookies) > 0
            
        except Exception:
            return False
    
    def _get_yt_dlp_version(self) -> str:
        """yt-dlp 버전 확인"""
        try:
            cmd = ["yt-dlp", "--version"]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
            
            if result.returncode == 0:
                return result.stdout.strip()
            else:
                return "알 수 없음"
                
        except Exception:
            return "알 수 없음"
    
    def _should_continue_after_success(self) -> bool:
        """성공 후에도 계속 진행할지 결정"""
        # 현재는 항상 계속 진행 (완벽한 해결을 위해)
        return True
    
    def _generate_final_summary(self) -> Dict[str, Any]:
        """최종 실행 결과 요약 생성"""
        logging.debug(f"\n{'='*60}")
        logging.debug("종합 솔루션 실행 결과 요약")
        logging.debug(f"{'='*60}")
        
        # 성공/실패 통계
        successful_solutions = [k for k, v in self.solution_results.items() if v['success']]
        failed_solutions = [k for k, v in self.solution_results.items() if not v['success']]
        
        logging.debug(f"성공한 해결 방안: {len(successful_solutions)}/{self.total_steps}")
        logging.debug(f"실패한 해결 방안: {len(failed_solutions)}/{self.total_steps}")
        
        # 각 방안별 결과
        for solution_key, result in self.solution_results.items():
            solution_name = self.solutions[solution_key]['name']
            status = " 성공" if result['success'] else " 실패"
            execution_time = f"{result['execution_time']:.2f}초"
            
            logging.debug(f"• {solution_name}: {status} ({execution_time})",
                         print_color="green" if result['success'] else "red")
            
            if not result['success']:
                logging.debug(f"{result['message']}")
        
        # 최종 권장사항
        if successful_solutions:
            logging.debug(f"\n 권장사항:")
            logging.debug(f"• 성공한 해결 방안을 사용하여 다운로드를 진행하세요.")
            
            if len(successful_solutions) > 1:
                logging.debug(f"• 여러 방안이 성공했으므로 가장 적합한 방법을 선택하세요.")
        else:
            logging.debug(f"\n️ 주의사항:")
            logging.debug(f"• 모든 해결 방안이 실패했습니다.")
            logging.debug(f"• 수동으로 문제를 해결하거나 다른 접근 방식을 시도해보세요.")
        
        # 결과 반환
        return {
            'total_solutions': self.total_steps,
            'successful_solutions': len(successful_solutions),
            'failed_solutions': len(failed_solutions),
            'success_rate': len(successful_solutions) / self.total_steps,
            'results': self.solution_results,
            'recommendations': self._generate_recommendations(successful_solutions, failed_solutions)
        }
    
    def _generate_recommendations(self, successful_solutions: List[str], failed_solutions: List[str]) -> List[str]:
        """권장사항 생성"""
        recommendations = []
        
        if successful_solutions:
            recommendations.append("성공한 해결 방안을 사용하여 다운로드를 진행하세요.")
            
            if 'solution_2' in successful_solutions:
                recommendations.append("새로운 쿠키가 생성되었으므로 연령 제한 동영상 다운로드가 가능할 것입니다.")
            
            if 'solution_4' in successful_solutions:
                recommendations.append("yt-dlp가 최신 버전으로 업데이트되었으므로 호환성 문제가 해결되었을 것입니다.")
        
        if failed_solutions:
            if 'solution_1' in failed_solutions:
                recommendations.append("Windows 환경 실행에 문제가 있으므로 WSL 환경에서 계속 진행하세요.")
            
            if 'solution_2' in failed_solutions:
                recommendations.append("쿠키 생성에 실패했으므로 수동으로 Chrome에서 쿠키를 내보내세요.")
        
        return recommendations


@ensure_seconds_measured
def ensure_youtube_comprehensive_solution_execution(test_url: str = None) -> bool:
    """
    YouTube 연령 제한 동영상 다운로드 종합 솔루션 실행
    
    Args:
        test_url: 테스트할 YouTube URL (None이면 기본 URL 사용)
        
    Returns:
        bool: 전체 솔루션 실행 성공 여부
    """
    # 종합 솔루션 실행기 생성
    solution_executor = ComprehensiveYouTubeSolution()
    
    # 모든 해결 방안 실행
    final_summary = solution_executor.execute_all_solutions(test_url)
    
    # 성공률 확인
    success_rate = final_summary['success_rate']
    
    if success_rate > 0:
        logging.debug(f"\n 종합 솔루션 실행 완료! 성공률: {success_rate:.1%}")
        return True
    else:
        logging.debug(f"\n 종합 솔루션 실행 완료했지만 모든 방안이 실패했습니다.")
        return False


if __name__ == "__main__":
    # 테스트 실행
    if LTA:
        logging.debug("LTA 모드: 실제 실행 건너뜀")
        logging.debug("테스트를 실행하려면 LTA = False로 설정하세요.")
    else:
        logging.debug("YouTube 연령 제한 동영상 다운로드 종합 솔루션 테스트 시작")
        
        # 종합 솔루션 실행
        success = ensure_youtube_comprehensive_solution_execution()
        
        if success:
            logging.debug("종합 솔루션 테스트 성공!")
        else:
            logging.debug("종합 솔루션 테스트 실패!")

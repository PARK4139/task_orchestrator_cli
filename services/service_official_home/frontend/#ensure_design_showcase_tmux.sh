#!/bin/bash

echo "🎭 ensure_design_showcase_tmux.sh: tmux 환경에서 디자인 쇼케이스!"
echo "================================================================="

# tmux 세션 이름
SESSION_NAME="design_showcase"

# 기존 세션 종료
tmux kill-session -t $SESSION_NAME 2>/dev/null

# 새 tmux 세션 생성
tmux new-session -d -s $SESSION_NAME

# 윈도우 1: 개발 서버
tmux rename-window -t $SESSION_NAME:0 'Dev Server'
tmux send-keys -t $SESSION_NAME:0 'npm run dev' C-m

# 윈도우 2: 디자인 쇼케이스 로그
tmux new-window -t $SESSION_NAME -n 'Showcase Log'
tmux send-keys -t $SESSION_NAME:1 'echo "🎨 디자인 쇼케이스 로그 시작..."' C-m

# 윈도우 3: 디자인 전환 스크립트
tmux new-window -t $SESSION_NAME -n 'Design Switcher'

# 윈도우 4: 브라우저 모니터링
tmux new-window -t $SESSION_NAME -n 'Browser Monitor'
tmux send-keys -t $SESSION_NAME:3 'echo "🌐 브라우저에서 http://localhost:3000 확인하세요!"' C-m
tmux send-keys -t $SESSION_NAME:3 'echo "⏱️  10초마다 디자인이 자동으로 변경됩니다"' C-m

# 디자인 전환 스크립트 실행
tmux send-keys -t $SESSION_NAME:2 './ensure_design_showcase_hotreload.sh' C-m

# 창 분할 및 실시간 로그
tmux split-window -t $SESSION_NAME:1 -h
tmux send-keys -t $SESSION_NAME:1.1 'tail -f ../build_attempts_*.log 2>/dev/null || echo "로그 대기중..."' C-m

# tmux 세션 attach
echo ""
echo "🚀 tmux 세션 '$SESSION_NAME' 생성 완료!"
echo ""
echo "📋 사용법:"
echo "   • tmux attach -t $SESSION_NAME    (세션 접속)"
echo "   • Ctrl+B, w                      (윈도우 목록)"
echo "   • Ctrl+B, c                      (새 윈도우)"
echo "   • Ctrl+B, d                      (세션 분리)"
echo "   • tmux kill-session -t $SESSION_NAME  (세션 종료)"
echo ""
echo "🎯 윈도우 구성:"
echo "   0: Dev Server      (개발 서버)"
echo "   1: Showcase Log    (쇼케이스 로그)"  
echo "   2: Design Switcher (디자인 전환기)"
echo "   3: Browser Monitor (브라우저 모니터)"
echo ""

# 자동으로 세션에 연결
tmux attach -t $SESSION_NAME 
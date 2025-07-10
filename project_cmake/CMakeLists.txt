# CMake 최소 버전 설정
cmake_minimum_required(VERSION 3.28)

# 프로젝트 이름 및 언어 설정
project(project_cmake)

# C++ 표준 설정
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED True)

# 디버깅을 위한 컴파일 옵션 추가 (-g: 디버깅 심볼 포함, -O0: 최적화 비활성화)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -g -O0")

# 실행 파일을 bin 폴더에 생성하도록 설정
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/bin)

# 실행 파일 생성
add_executable(project_cmake src/main.cpp src/core.cpp)

# yaml-cpp 설정 (시스템 경로에서 자동으로 찾도록 설정)
find_package(yaml-cpp REQUIRED)

# yaml-cpp 라이브러리 연결
target_link_libraries(project_cmake PRIVATE yaml-cpp)

# config.yaml을 실행 파일 폴더로 복사
add_custom_command(
    TARGET project_cmake POST_BUILD
    COMMAND ${CMAKE_COMMAND} -E copy
    ${CMAKE_SOURCE_DIR}/src/config.yaml
    ${CMAKE_RUNTIME_OUTPUT_DIRECTORY}/config.yaml
)

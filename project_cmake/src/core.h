#ifndef ADD_CORE //header guarder s : 헤더 파일이 여러 번 포함되는 것을 방지
#define ADD_CORE //define ADD_CORE, 또다시 define ADD_CORE 되는 것은 무시

// include
#include <iostream> // std::cout, std::endl 내장 lib
#include <cstdlib>  // system() 내장 lib
#include <cstdio>  // popen(), pclose(), printf() 내장 lib (c 스타일 formatting 기능)
#include <memory>  // std::unique_ptr
#include <array>   // std::array
//#include <format>  // std::format 내장 lib, // C++ 20 이상 사용가능 (Python의 f-string처럼 문자열 포매팅이 가능한)
#include <string> // std::string 내장
#include <cstdarg>   // va_list, va_start, va_end
#include <vector> 
#include <sstream> // std::istringstream
#include <iostream>
#include <string>
#include <yaml-cpp/yaml.h>



struct Config {
    // 구조체를 정의하고, 구조체 메소드를 통하여 구조체 인스턴스에 파일의 값을 가져와 초기화한다
    int max_value;
    int min_value;
    int default_value;
     
    double pi;
    double e;
    double gravity;

    std::string app_name;
    std::string version;
    std::string author;

    bool debug_mode;
    bool verbose_logging;

    void loadConfigFromFile(const std::string& f_nx) {
        YAML::Node config = YAML::LoadFile(f_nx);

        // 정수 값 초기화
        max_value = config["integers"]["max_value"].as<int>();
        min_value = config["integers"]["min_value"].as<int>();
        default_value = config["integers"]["default_value"].as<int>();

        // 실수 값 초기화
        pi = config["floats"]["pi"].as<double>();
        e = config["floats"]["e"].as<double>();
        gravity = config["floats"]["gravity"].as<double>();

        // 문자열 값 초기화
        app_name = config["strings"]["app_name"].as<std::string>();
        version = config["strings"]["version"].as<std::string>();
        author = config["strings"]["author"].as<std::string>();

        // 불리언 값 초기화
        debug_mode = config["booleans"]["debug_mode"].as<bool>();
        verbose_logging = config["booleans"]["verbose_logging"].as<bool>();
    }
};

// function declaration 함수 선언
int add(int a, int b);
std::string cmd_to_os(const std::string& cmd);
bool is_format_supported();
std::string get_hello_world();
std::string get_cpp_standard();
// void pk_print(std::string);
void pk_print(const char* prompt, ...) ;
void pk_print(const std::string& prompt); // std::string 지원을 위한 오버로딩


#endif //header guarder e : 헤더 파일이 여러 번 포함되는 것을 방지


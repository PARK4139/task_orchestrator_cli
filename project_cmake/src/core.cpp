#include "core.h" // include f_header


// function defination
int add(int a, int b) {
    return a + b;
}

std::string get_hello_world() {
    return "HELLO WORLD";
}


bool is_format_supported() {
    #if defined(__cpp_lib_format)  // C++20 이상에서 format 지원 여부 확인
        return true;
    #else
        return false;
    #endif
}

std::string cmd_to_os(const std::string& cmd) {
    std::array<char, 128> buffer;
    std::string std_str;
    std::string stamp_debug = "[CPP DEBUG]";

    pk_print("%s cmd=%s",stamp_debug.c_str(), cmd.c_str()); 

    // popen() //C-스타일 문자열 인자설정제한 // cmd.c_str() 
    std::unique_ptr<FILE, int(*)(FILE*)> pipe(popen(cmd.c_str(), "r"), pclose);
    if (!pipe) {
        std::cerr << "Failed to execute cmd" << std::endl;
        return "FAIL";
    }
    while (fgets(buffer.data(), buffer.size(), pipe.get()) != nullptr) {
        std_str += buffer.data();
    }
    // std::cout << "[std_str] " << std_str << std::endl;
    // pk_print("[std_str] %s",std_str); //fail
    // pk_print("[std_str] %s", std_str.c_str()); //success, but NG for reading

    std::vector<std::string> std_vector;
    std::istringstream stream(std_str);
    std::string line;

    // 한 줄씩 읽어서 vector에 추가
    while (std::getline(stream, line)) {
        std_vector.push_back(line);
    }

    // 출력 (for-each 루프 사용)
    for (const auto& std_str : std_vector) {
        pk_print("[STD_STR] %s", std_str.c_str()); 
    }
    
    return std_str; 
}


// c++20 이상/std::format 내장
// template<typename... Args>
// void pk_print(const std::string& format_str, Args&&... args) {
//     std::cout << std::format(format_str, std::forward<Args>(args)...) << std::endl;
// }
void pk_print(const char* prompt, ...) {
    constexpr size_t BUFFER_SIZE = 1024;  // 버퍼 크기 설정
    char buffer[BUFFER_SIZE];

    // 가변 인자 처리
    va_list args;
    va_start(args, prompt);
    vsnprintf(buffer, BUFFER_SIZE, prompt, args);  // 포맷팅된 문자열을 buffer에 저장
    va_end(args);

    // 출력
    std::cout << buffer << std::endl;
}
void pk_print(const std::string& prompt) {
    // std::string 지원을 위한 오버로딩
    std::cout << prompt << std::endl;
}

std::string get_cpp_standard() {
    // __cplusplus 값에 따라 C++ 표준 버전 판별
    if (__cplusplus == 199711L) {
        return "C++98";
    } else if (__cplusplus == 201103L) {
        return "C++11";
    } else if (__cplusplus == 201402L) {
        return "C++14";
    } else if (__cplusplus == 201703L) {
        return "C++17";
    } else if (__cplusplus == 202002L) {
        return "C++20";
    } else if (__cplusplus == 202302L) {
        return "C++23";
    } else if (__cplusplus > 202302L) {
        return "Future C++ version";
    } else {
        return "Unknown C++ standard";
    }
}

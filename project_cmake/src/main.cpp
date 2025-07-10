// vscode summary
// F2 : rename refactoring
// F12 : go to Definition
// ctrl F12 : go to Declaration
// ctrl shift b: run 
// settings.json 에서는 IDEA(VSCODE), IDEA PLUGIN(VSCODE EXTENSION)을 셋팅하는 파일 같다.
// 단축키가 안먹은 경우 : wsl 환경에 별도로 clang, c/c++, c/c++ extension 을 install  

// c++ summary
// src/core.h
// src/core.cpp
// src/main.cpp/main()
// cpp에서는 속도를 위해서 f.h 와 f.cpp 을 나눠서 function declaration/defination을 작성
// f.h 와 f.cpp 는 하나의 셋트 작성되어야 하는 것으로 보인다.

#include "core.h" // custom lib

void test_done() {
    // print 
    // std::cout << get_hello_world() << std::endl;  
    // << = operator to insert
    // std::cout = print std output char stream at console
    // std::endl = print linefeed '\n' and flush(출력버퍼 강제 비워기))
    pk_print(get_hello_world());

    // g++ --version
    std::string std_str;
    std::string cmd; 
    cmd = "g++ --version";
    std_str = cmd_to_os(cmd);
    pk_print(std_str);

    // cpp --version
    pk_print(get_cpp_standard());

    // control c++ logic flow 
    if (is_format_supported()) {
        pk_print("std::<format> is supported in this compiler.\n");
    } else {
        pk_print("std::<format> is NOT supported in this compiler");
    }

    // formatting
    int x = 10;
    int y = 5;
    int result = add(x, y);
    // std::cout << x << " + " << y << " = " << result << std::endl; // formatting 불편, 가독성 낮음
    // printf("%d + %d = %d\n", x, y, result); // c style formatting // formatting 불편, 가독성 보통
    // std::cout << std::format("{} + {} = {}\n", x, y, result); # C++ 20 이상만 std::format 지원 // formatting 보통불편, 가독성 보통
    pk_print("%d + %d = %d\n", x, y, result);

    // cmd
    cmd_to_os("ls -alh");
    cmd_to_os("pwd");

    // yaml-cpp install
    cmd_to_os("sudo apt update> /dev/null 2>&1");
    cmd_to_os("echo y | sudo apt install libyaml-cpp-dev");
    cmd_to_os("dpkg -s libyaml-cpp-dev");
}

void test_todo() {
    // cold data Proposal 1
    // migrate constants.py to data_cold.h and data_cold.cpp
    // 상수는 전처리기로 정의, run time 최적화에 힘을 쓸수 있는거 아닌가?

    // cold data Proposal 2
    // 컴파일타임과 런타임 중 변경되지 않을 상수 데이터를 중점 관리
    // constexpr 와 yaml 의 조합으로 cold data 관리
    // data_cold.yaml + main.cpp/constexpr 
    // migrate constants.py to data_cold.yaml
    // LOCAL_ACTIVATE_MODE = 1  // debug mode
    
    // hot data 관리
    // LOCAL CONSTANT 로 SCOPE를 최대한 좁혀서 사용.
    
    // pointer 사용

    // a2z config 관리방식 관찰

    // a2z autodrive rule 관찰
    // 1 : ON
    // 0 : OFF

    //코드시간측정
    //타임스탬프 

    //sleep()
}


void test_work() {
    Config config;
    try {
        // config.loadFromF("../src/config.yaml"); // pwd = project/build 
        config.loadConfigFromFile("config.yaml");
    } catch (const std::exception& e) {
        pk_print("⚠️ ERROR: Failed to load config file: %s", e.what());
    }
    pk_print("1"); 
    pk_print("1"); 
    pk_print("1"); 
    pk_print("1"); 
    pk_print("1"); 
    pk_print(config.app_name); 
    pk_print("1"); 
    pk_print("1"); 
    pk_print("1"); 
    pk_print("1"); 
    pk_print("1"); 



    // `festd::cout << "Max Value: " << config.max_value << ", PI: " << config.pi << std::endl;
    // std::cout << "Debug Mode: " << (config.debug_mode ? "Enabled" : "Disabled") << std::endl;
}
 
int main() {
    // test_done();    
    test_work();
    return 0;
}
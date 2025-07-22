# 数控机床驱动源码（第二版）

本项目为第二版数控机床的驱动源码，基于 Raspberry Pi 作为主控单元，结合步进电机、直流电机、红外传感器、压力传感器、NFC 等多种外设，实现核心控制功能。项目涵盖 PCB 接线、进程与通信、PyQt5 界面设计等多项技术，适用于数控机床的教学与开发。

## 项目简介
- **主控平台**：Raspberry Pi
- **主要外设**：步进电机、直流电机、红外传感器、压力传感器、NFC
- **核心功能**：多外设协同控制、数据采集与处理、图形化界面操作
- **技术栈**：Python 3、PyQt5、串口通信、多线程/多进程

## 主要功能
- 步进电机与直流电机的精准控制
- 红外、压力等多种传感器数据采集
- NFC 识别与交互
- 设备状态实时监控与日志记录
- 基于 PyQt5 的可视化操作界面

## 目录结构说明
```text
motorbed_ui_py/
├── Controlls/         # 控制器相关代码
│   └── Control.py
├── DCMotors/          # 直流电机驱动
│   └── DCMotor.py
├── Define.py          # 全局常量与定义
├── interface.py       # 主界面逻辑
├── interface.ui       # Qt Designer 设计的界面文件
├── MagnetSensors/     # 磁传感器驱动
│   └── MagnetSensor.py
├── My_interface.py    # 自定义界面逻辑
├── Peripherals/       # 外设抽象层
│   └── Peripheral.py
├── PressSensors/      # 压力传感器驱动
│   └── PressSensor.py
├── PushRods/          # 推杆驱动
│   └── PushRod.py
├── RedSensors/        # 红外传感器驱动
│   └── RedSensor.py
├── Serials/           # 串口通信
│   └── Serial.py
├── Servers/           # 服务端/通信服务
│   └── Server.py
├── Source/            # 资源文件（图片等）
│   └── luo.jpg
├── Source_rc.py       # Qt 资源文件（Python 版）
├── Source.qrc         # Qt 资源文件
├── Stepmotors/        # 步进电机驱动
│   └── StepMotor.py
└── __init__.py        # 包初始化
```

## 项目框架

本项目采用分层模块化设计，结构清晰，便于维护和扩展。各层说明如下：

1. **界面层（UI Layer）**
   - 主要文件：`interface.py`, `interface.ui`, `My_interface.py`
   - 作用：基于 PyQt5 实现图形化操作界面，负责与用户交互，展示设备状态、日志信息，并将用户指令传递给控制层。

2. **控制层（Control Layer）**
   - 主要文件：`Controlls/Control.py`
   - 作用：协调各类外设的工作流程，实现核心业务逻辑，如运动控制、数据采集、状态管理等。

3. **驱动层（Driver Layer）**
   - 主要文件及目录：
     - 步进电机：`Stepmotors/StepMotor.py`
     - 直流电机：`DCMotors/DCMotor.py`
     - 红外传感器：`RedSensors/RedSensor.py`
     - 压力传感器：`PressSensors/PressSensor.py`
     - 磁传感器：`MagnetSensors/MagnetSensor.py`
     - 推杆：`PushRods/PushRod.py`
   - 作用：每种外设有独立驱动模块，负责底层硬件的初始化、控制和数据采集，向上层提供统一接口。

4. **外设抽象层（Peripheral Abstraction Layer）**
   - 主要文件：`Peripherals/Peripheral.py`
   - 作用：对各类外设进行抽象，定义统一接口规范，便于控制层调用和扩展新设备。

5. **通信与服务层（Communication & Service Layer）**
   - 主要文件及目录：
     - 串口通信：`Serials/Serial.py`
     - 服务端/通信服务：`Servers/Server.py`
   - 作用：实现与外部设备或上位机的数据通信，支持串口、网络等多种方式。

6. **资源与配置（Resources & Config）**
   - 主要文件及目录：
     - 资源文件：`Source/luo.jpg`, `Source.qrc`, `Source_rc.py`
     - 全局定义：`Define.py`
   - 作用：存放图片、配置、全局常量等资源文件。

7. **包初始化**
   - 文件：`__init__.py`
   - 作用：标识包结构，便于模块导入。

---

## 快速开始
1. **环境准备**
   - 安装依赖：`pip install pyqt5 pyserial`
2. **运行主界面**
   ```bash
   python interface.py
   ```
3. **硬件连接**
   - 按照 PCB 接线图连接各外设至 Raspberry Pi
   - 确认串口、GPIO 等接口配置正确

## 联系方式
- 作者：本人独立开发
- 邮箱：xiaoluo37o8@163.com

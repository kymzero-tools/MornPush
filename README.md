# 晓风知晴 (MornPush) ☀️

> 每日清晨，为你推送第一缕天气资讯。基于高德天气 API 与 PushDeer 的轻量级定时推送工具。

![GitHub Actions](https://img.shields.io/github/actions/workflow/status/YOUR_USERNAME/YOUR_REPO/weather-push.yml?branch=main&label=Daily%20Push)
![Python](https://img.shields.io/badge/Python-3.11-blue)
![License](https://img.shields.io/badge/License-MIT-green)

## 📖 项目简介

**晓风知晴 (MornPush)** 是一个极简的自动化天气推送脚本。它利用 GitHub Actions 提供的免费定时任务（Cron）能力，每天早晨 7:00（北京时间）自动获取指定城市的实时天气，并通过 PushDeer 推送到你的手机、电脑或智能手表上。

无需服务器，无需常驻后台，Fork 即用。

## ✨ 功能特性

-   🌤️ **实时天气**：调用高德地图官方 API，数据准确稳定。
-   ⏰ **定时唤醒**：基于 GitHub Actions 定时触发，每天早安问候不迟到。
-   📱 **多端推送**：依托 PushDeer，支持 iOS、Android、Mac、Windows 及微信通知。
-   🛠️ **零成本部署**：纯云端运行，无需购买服务器，配置 Secrets 即可完成部署。
-   🎨 **Markdown 渲染**：推送内容支持 Markdown 格式，排版清晰美观。

---

## 🚀 快速开始 (部署指南)

### 1. 前置准备

在开始之前，你需要准备两个 Key：

-   **高德 Web服务 Key**：前往 [高德开放平台](https://console.amap.com/dev/key/app) 注册并创建应用，生成 `Web服务` 类型的 Key。
-   **PushDeer Key**：前往 [PushDeer 官网](https://www.pushdeer.com/) 或下载 App，获取你的专属 `PushKey`。

### 2. Fork 本仓库

点击本仓库右上角的 **Fork** 按钮，将项目克隆到你自己的 GitHub 账号下。

### 3. 配置 Secrets (核心步骤)

进入你 Fork 后的仓库，依次点击 **Settings** -> **Secrets and variables** -> **Actions**，点击 **New repository secret** 添加以下三个环境变量：

| Secret 名称      | 说明                     | 示例值                 | ⚠️ 注意事项                              |
| :--------------- | :----------------------- | :--------------------- | :--------------------------------------- |
| `AMAP_KEY`       | 高德开放平台 Web服务 Key | `a1b2c3d4e5f6g7h8...`  | 必须是 **Web服务** 类型                  |
| `PUSHDEER_KEY`   | PushDeer 的推送 Key      | `PDU12345T67890...`    | 确保 App 已登录并开启通知                |
| `CITY`           | 需要查询天气的城市       | `杭州` 或 `330100`     | **必须是中文或 adcode，切勿使用拼音！**  |

### 4. 开启 Actions 权限

由于 Fork 的仓库默认关闭 Actions，请进入仓库的 **Actions** 页面，点击 **"I understand my workflows, go ahead and enable them"** 开启工作流。

### 5. 手动触发测试

在 **Actions** 页面左侧选择 `每日天气推送`，点击右侧的 **Run workflow** 按钮手动执行一次。如果日志显示 `✅ PushDeer 推送成功！`，说明部署完美成功！🎉

---

## 📂 项目结构

```text
├── .github/
│   └── workflows/
│       └── weather-push.yml  # GitHub Actions 定时任务配置
├── weather_push.py           # 核心 Python 脚本
├── requirements.txt          # Python 依赖 (仅 requests)
├── README.md                 # 项目说明文档
└── LICENSE                   # MIT 开源协议
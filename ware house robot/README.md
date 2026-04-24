# 🚀 Warehouse Robot using Q-Learning

## 📌 Overview

This project simulates an intelligent warehouse robot that learns to pick up and deliver items using **Q-learning (Reinforcement Learning)**.

The robot navigates a grid environment with obstacles and optimizes its path through trial-and-error learning.

---

## 🎯 Features

* 🤖 Q-learning based decision making
* 🖱️ Mouse-click interactive pickup & drop selection
* 🔲 Obstacle avoidance
* 📊 Learning performance graph
* 🎮 Real-time grid visualization

---

## 🧠 How It Works

* The environment is modeled as a grid
* The agent learns using a **Q-table**
* Rewards:

  * +20 → Pickup item
  * +50 → Deliver item
  * -1 → Each step

The agent improves its policy over multiple episodes.

---

## 📁 Project Structure

```
Warehouse-Robot-RL/
│
├── src/
│   ├── environment.py
│   ├── agent.py
│   ├── visualization.py
│   └── main.py
│
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

```bash
git clone <your-repo-link>
cd Warehouse-Robot-RL
pip install -r requirements.txt
```

---

## ▶️ Run the Project

```bash
python src/main.py
```

---

## 🎮 Usage

1. A grid window will open
2. Click:

   * First → Pickup location
   * Second → Drop location
3. The robot will learn and simulate the task

---

## 📊 Output

* Learning curve (reward vs episodes)
* Animated robot movement

---

## 🧾 Resume Description

> Developed an interactive Q-learning based warehouse robot simulation with obstacle avoidance, dynamic environment configuration, and real-time visualization using Python and Matplotlib.

---

## 🚀 Future Improvements

* Deep Q-Learning (DQN)
* Multiple robots (multi-agent system)
* GUI using Pygame

---

## 👨‍💻 Author

Imtiaz Hussain

#include <stdio.h>
#include <conio.h>
#include <windows.h>

int main() {
    int playerPos = 10; // 玩家初始位置
    int obstaclePos = 30; // 障礙物初始位置
    int score = 0; // 分數

    while(1) {
        system("cls"); // 清空終端

        // 在終端上繪製玩家和障礙物
        for (int i = 0; i < 40; ++i) {
            if (i == playerPos) {
                printf("P");
            } else if (i == obstaclePos) {
                printf("X");
            } else {
                printf(" ");
            }
        }

        // 檢查是否碰到障礙物
        if (playerPos == obstaclePos) {
            printf("\nGame Over! Final Score: %d\n", score);
            break;
        }

        // 如果沒有碰到障礙物，增加分數並移動障礙物
        ++score;
        ++obstaclePos;

        // 檢查是否超出邊界，如果是，重新設定障礙物位置
        if (obstaclePos >= 40) {
            obstaclePos = 0;
        }

        // 檢測鍵盤輸入來移動玩家
        if (_kbhit()) {
            char key = _getch();
            if (key == 'a' && playerPos > 0) {
                --playerPos; // 向左移動玩家
            } else if (key == 'd' && playerPos < 39) {
                ++playerPos; // 向右移動玩家
            }
        }

        Sleep(100); // 控制遊戲速度
    }

    return 0;
}

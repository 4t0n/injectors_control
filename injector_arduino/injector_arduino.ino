#include <PWM.h>
#include <GyverFIFO.h>
#include <FIFO.h>
#include <GStypes.h>
#include <GParser.h>
#include <parseUtils.h>
#include <unicode.h>
#include <url.h>
#include <AsyncStream.h>
#define outPWM 9 // пин для генератора сигналов (не менять) - это выход на Мосфет управления форсунками.

AsyncStream<50> serial(&Serial, ';');
unsigned int frequency = 1; // стартовое значение частоты в Гц
byte duty = 0;    // стартовое значение заполнения (0...255)
bool start_status = 0;

void setup()
{
    Serial.begin(115200);
    InitTimersSafe();
    SetPinFrequencySafe(outPWM, frequency);
}

void loop()
{
    parsing();
}

void PWMrefresh()
{
    SetPinFrequencySafe(outPWM, frequency);
    pwmWrite(outPWM, duty);
}

void parsing()
{
    if (serial.available())
    {
        GParser data(serial.buf, ',');
        long ints[10];
        data.parseLongs(ints);
        switch (ints[0])
        {
        case 0: // изменение частоты сигнала
            if (ints[1] < 1)
            {
                frequency = 1;
            }
            if (ints[1] > 500)
            {
                frequency = 500;
            }
            if (start_status)
            {
                PWMrefresh();
            }
            break;
        case 1: // изменение заполнения сигнала
        {
            if (ints[1] < 0)
            {
                duty = 0;
            }
            if (ints[1] > 255)
            {
                duty = 255;
            }
            if (start_status)
            {
                PWMrefresh();
            }
            break;
        }
        case 2: // запуск работы
        {
            start_status = 1;
            PWMrefresh();
            break;
        }
        case 3: // стоп
        {
            start_status = 0;
            pwmWrite(outPWM, 0);
            break;
        }
        }
    }
}

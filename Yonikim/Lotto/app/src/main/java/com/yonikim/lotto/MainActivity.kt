package com.yonikim.lotto

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.os.CountDownTimer
import android.widget.Button
import android.widget.TextView
import com.airbnb.lottie.LottieAnimationView

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val lottoNumber1 = findViewById<TextView>(R.id.lottoNumber1)
        val lottoNumber2 = findViewById<TextView>(R.id.lottoNumber2)
        val lottoNumber3 = findViewById<TextView>(R.id.lottoNumber3)
        val lottoNumber4 = findViewById<TextView>(R.id.lottoNumber4)
        val lottoNumber5 = findViewById<TextView>(R.id.lottoNumber5)
        val lottoNumber6 = findViewById<TextView>(R.id.lottoNumber6)

        val lottoNumbers = arrayListOf(
            lottoNumber1,
            lottoNumber2,
            lottoNumber3,
            lottoNumber4,
            lottoNumber5,
            lottoNumber6
        )
        val countDownTimer = object : CountDownTimer(3000, 100) {
            override fun onTick(millisUntilFinished: Long) {
                lottoNumbers.forEach {
                    val randomNumber = (Math.random() * 45 + 1).toInt()
                    it.text = "$randomNumber"
                }
            }
            override fun onFinish() {
            }

        }

        val lottoButton = findViewById<LottieAnimationView>(R.id.lottoButton)
        lottoButton.setOnClickListener {
            if (lottoButton.isAnimating) {
                lottoButton.cancelAnimation()
                countDownTimer.cancel()
            } else {
                lottoButton.playAnimation()
                countDownTimer.start()
            }

        }

    }
}
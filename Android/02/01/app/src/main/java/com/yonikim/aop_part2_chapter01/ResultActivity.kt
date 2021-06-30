package com.yonikim.aop_part2_chapter01

import android.os.Bundle
import android.util.Log
import android.widget.TextView
import androidx.appcompat.app.AppCompatActivity
import kotlin.math.pow

class ResultActivity: AppCompatActivity() {

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_result)

        val height = intent.getIntExtra("height", -1)
        val weight = intent.getIntExtra("weight", -1)
        Log.d("ResultActivity", "height: $height, weight: $weight")

        val bmi = weight / (height / 100.0).pow(2.0) // = Math.pow(double, double)
        val resultText = when {
            bmi >= 35.0 -> "고도 비만"
            bmi >= 30.0 -> "중정도 비만"
            bmi >= 25.0 -> "경도 비만"
            bmi >= 23.0 -> "과체중"
            bmi >= 18.5 -> "정상체중"
            else -> "저체중"
        }

        val bmiTextView = findViewById<TextView>(R.id.bmiTextView)
        val bmiResultTextView = findViewById<TextView>(R.id.bmiResultTextView)

        bmiTextView.text = bmi.toString()
        bmiResultTextView.text = resultText
    }

}
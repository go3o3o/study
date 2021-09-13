package com.yonikim.lotto

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.os.Handler
import android.os.Looper
import com.airbnb.lottie.LottieAnimationView

class SplashActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_splash)


        val handler = Handler(Looper.getMainLooper())
        val runnable = Runnable {
            goMainActivity()
        }
        handler.postDelayed(runnable, 3000)

        val animationView = findViewById<LottieAnimationView>(R.id.animationView)
        animationView.setOnClickListener {
            handler.removeCallbacks(runnable)
            goMainActivity()
        }

    }

    private fun goMainActivity() {
        val intent = Intent(this, MainActivity::class.java)
        startActivity(intent)
        finish()
    }
}
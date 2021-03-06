package com.yonikim.lotto

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.os.CountDownTimer
import android.os.Handler
import android.os.Looper
import android.util.Log
import com.airbnb.lottie.LottieAnimationView

class LoadingActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_loading)


        val handler = Handler(Looper.getMainLooper())
        val runnable = Runnable {
            goMainActivity()
        }
        handler.postDelayed(runnable, 5000)

        val animationView = findViewById<LottieAnimationView>(R.id.animationView)
        animationView.setOnClickListener {
            handler.removeCallbacks(runnable)
            goMainActivity()
        }

        val appNameTextView = findViewById<TypingWriter>(R.id.appNameTextView)
        appNameTextView.setText("")
        appNameTextView.setCharacterDelay(150)
        appNameTextView.animateText(resources.getString(R.string.app_name))
    }

    private fun goMainActivity() {
        val intent = Intent(this, DesireActivity::class.java)
        startActivity(intent)
        finish()
    }


}
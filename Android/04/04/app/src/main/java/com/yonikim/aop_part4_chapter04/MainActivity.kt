package com.yonikim.aop_part4_chapter04

import android.content.Context
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.util.TypedValue
import androidx.constraintlayout.motion.widget.MotionLayout
import com.yonikim.aop_part4_chapter04.databinding.ActivityMainBinding

class MainActivity : AppCompatActivity() {

    val binding by lazy {
        ActivityMainBinding.inflate(layoutInflater)
    }
    private var isGatheringMotionAnimating: Boolean = false

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        binding.scrollView.viewTreeObserver.addOnScrollChangedListener {
            if (binding.scrollView.scrollY > 150f.dpToPx(this).toInt()) {
                if (isGatheringMotionAnimating.not()) {
                    binding.gatheringDigitalThingsMotionLayout.transitionToEnd()
                }
            } else {
                if (isGatheringMotionAnimating.not()) {
                    binding.gatheringDigitalThingsMotionLayout.transitionToStart()
                }
            }
        }
        binding.gatheringDigitalThingsMotionLayout.setTransitionListener(object :
            MotionLayout.TransitionListener {
            override fun onTransitionStarted(
                motionLayout: MotionLayout?,
                startId: Int,
                endId: Int
            ) {
                isGatheringMotionAnimating = TRUE
            }

            override fun onTransitionChange(
                motionLayout: MotionLayout?,
                startId: Int,
                endId: Int,
                progress: Float
            ) = Unit

            override fun onTransitionCompleted(motionLayout: MotionLayout?, currentId: Int) {
                isGatheringMotionAnimating = false
            }

            override fun onTransitionTrigger(
                motionLayout: MotionLayout?,
                triggerId: Int,
                positive: Boolean,
                progress: Float
            ) = Unit

        })
    }

    private fun Float.dpToPx(context: Context): Float =
        TypedValue.applyDimension(
            TypedValue.COMPLEX_UNIT_DIP,
            this,
            context.resources.displayMetrics
        )
}
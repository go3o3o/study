package com.yonikim.aop_part3_chapter04

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import androidx.room.Room
import com.bumptech.glide.Glide
import com.yonikim.aop_part3_chapter04.Model.Book
import com.yonikim.aop_part3_chapter04.Model.Review
import com.yonikim.aop_part3_chapter04.databinding.ActivityDetailBinding

class DetailActivity : AppCompatActivity() {

    private lateinit var binding: ActivityDetailBinding

    private lateinit var db: AppDatabase

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        binding = ActivityDetailBinding.inflate(layoutInflater)
        setContentView(binding.root)

        db = getAppDatabase(this)

        val model = intent.getParcelableExtra<Book>("bookModel")
        binding.titleTextView.text = model?.title.orEmpty()
        binding.descriptionTextView.text = model?.description.orEmpty()

        Glide.with((binding.coverImageView.context))
            .load(model?.coverSmallUrl.orEmpty())
            .into(binding.coverImageView)

        Thread {
            val review = db.reviewDao().getReview(model?.id?.toInt() ?: 0)
            runOnUiThread {
                binding.reviewEditText.setText(review?.review.orEmpty())
            }
        }.start()

        binding.saveButton.setOnClickListener {
            Thread {
                db.reviewDao().saveReview(
                    Review(
                        model?.id?.toInt() ?: 0,
                        binding.reviewEditText.text.toString()
                    )
                )
            }.start()
        }

    }
}
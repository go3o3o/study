package com.yonikim.aop_part3_chapter06.home

import android.view.LayoutInflater
import android.view.ViewGroup
import androidx.recyclerview.widget.DiffUtil
import androidx.recyclerview.widget.ListAdapter
import androidx.recyclerview.widget.RecyclerView
import com.bumptech.glide.Glide
import com.yonikim.aop_part3_chapter06.databinding.ArticleItemBinding
import java.text.SimpleDateFormat
import java.util.*

class ArticleAdapter : ListAdapter<ArticleModel, ArticleAdapter.ViewHolder>(diffUtil) {
    inner class ViewHolder(private val binding: ArticleItemBinding) :
        RecyclerView.ViewHolder(binding.root) {
        fun bind(articleModel: ArticleModel) {

            val format = SimpleDateFormat("yy년 MM월 dd일")
            val createdAt = Date(articleModel.createdAt)

            binding.titleTextView.text = articleModel.title
            binding.createdAtTextView.text = format.format(createdAt).toString()
            binding.priceTextView.text = articleModel.price
            if (articleModel.imageUrl.isNotEmpty()) {
                Glide.with(binding.thumbnailImageView)
                    .load(articleModel.imageUrl)
                    .into(binding.thumbnailImageView)
            }
        }
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ViewHolder {
        return ViewHolder(
            ArticleItemBinding.inflate(
                LayoutInflater.from(parent.context),
                parent,
                false
            )
        )
    }

    override fun onBindViewHolder(holder: ViewHolder, position: Int) {
        holder.bind(currentList[position])
    }

    companion object {
        val diffUtil = object : DiffUtil.ItemCallback<ArticleModel>() {
            override fun areItemsTheSame(oldItem: ArticleModel, newItem: ArticleModel): Boolean {
                return oldItem.createdAt == newItem.createdAt
            }

            override fun areContentsTheSame(oldItem: ArticleModel, newItem: ArticleModel): Boolean {
                return oldItem == newItem
            }

        }
    }

}
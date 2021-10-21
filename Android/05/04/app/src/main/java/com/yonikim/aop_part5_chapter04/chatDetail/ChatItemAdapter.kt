package com.yonikim.aop_part5_chapter04.chatDetail


import android.view.LayoutInflater
import android.view.ViewGroup
import androidx.recyclerview.widget.DiffUtil
import androidx.recyclerview.widget.ListAdapter
import androidx.recyclerview.widget.RecyclerView
import com.yonikim.aop_part5_chapter04.databinding.ChatItemBinding

class ChatItemAdapter :
    ListAdapter<ChatItem, ChatItemAdapter.ViewHolder>(
        ChatItemAdapter.diffUtil
    ) {
    inner class ViewHolder(private val binding: ChatItemBinding) :
        RecyclerView.ViewHolder(binding.root) {
        fun bind(chatItem: ChatItem) {
            binding.senderTextView.text = chatItem.senderId
            binding.messageTextView.text = chatItem.message

        }
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ViewHolder {
        return ViewHolder(
            ChatItemBinding.inflate(
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
        val diffUtil = object : DiffUtil.ItemCallback<ChatItem>() {
            override fun areItemsTheSame(oldItem: ChatItem, newItem: ChatItem): Boolean {
                return oldItem == newItem
            }

            override fun areContentsTheSame(oldItem: ChatItem, newItem: ChatItem): Boolean {
                return oldItem == newItem
            }

        }
    }
}
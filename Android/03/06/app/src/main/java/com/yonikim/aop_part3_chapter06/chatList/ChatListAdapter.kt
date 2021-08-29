package com.yonikim.aop_part3_chapter06.chatList

import ChatListItem
import android.view.LayoutInflater
import android.view.ViewGroup
import androidx.recyclerview.widget.DiffUtil
import androidx.recyclerview.widget.ListAdapter
import androidx.recyclerview.widget.RecyclerView
import com.yonikim.aop_part3_chapter06.databinding.ChatListItemBinding

class ChatListAdapter(val onItemClicked: (ChatListItem) -> Unit) :
    ListAdapter<ChatListItem, ChatListAdapter.ViewHolder>(
        ChatListAdapter.diffUtil
    ) {
    inner class ViewHolder(private val binding: ChatListItemBinding) :
        RecyclerView.ViewHolder(binding.root) {
        fun bind(chatListItem: ChatListItem) {
            binding.root.setOnClickListener {
                onItemClicked(chatListItem)
            }

            binding.chatRoomTitleTextView.text = chatListItem.itemTitle

        }
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ViewHolder {
        return ViewHolder(
            ChatListItemBinding.inflate(
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
        val diffUtil = object : DiffUtil.ItemCallback<ChatListItem>() {
            override fun areItemsTheSame(oldItem: ChatListItem, newItem: ChatListItem): Boolean {
                return oldItem.key == newItem.key
            }

            override fun areContentsTheSame(oldItem: ChatListItem, newItem: ChatListItem): Boolean {
                return oldItem == newItem
            }

        }
    }
}
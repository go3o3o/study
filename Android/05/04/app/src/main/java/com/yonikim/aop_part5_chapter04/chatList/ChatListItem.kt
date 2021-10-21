package com.yonikim.aop_part5_chapter04.chatList

data class ChatListItem(
    val buyerId: String,
    val sellerId: String,
    val itemTitle: String,
    val key: String
) {
    constructor(): this("", "", "", "")
}

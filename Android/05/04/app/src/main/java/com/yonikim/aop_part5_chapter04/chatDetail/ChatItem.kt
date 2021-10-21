package com.yonikim.aop_part5_chapter04.chatDetail

data class ChatItem(
    val senderId: String,
    val message: String,
    val createdAt: Long
) {
    constructor(): this("","",0)
}
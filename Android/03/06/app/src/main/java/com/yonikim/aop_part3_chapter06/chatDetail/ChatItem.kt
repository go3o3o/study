package com.yonikim.aop_part3_chapter06.chatDetail

data class ChatItem(
    val senderId: String,
    val message: String,
    val createdAt: Long
) {
    constructor(): this("","",0)
}

package com.yonikim.aop_part5_chapter01.data.repository

import com.yonikim.aop_part5_chapter01.data.entity.ToDoEntity

class TestToDoRepository : ToDoRepository {

    private val toDoList: MutableList<ToDoEntity> = mutableListOf()

    override suspend fun getToDoList(): List<ToDoEntity> {
        return toDoList
    }

    override suspend fun insertToDoItem(toDoEntity: ToDoEntity): Long {
        this.toDoList.add(toDoEntity)
        return toDoEntity.id
    }

    override suspend fun insertToDoList(toDoList: List<ToDoEntity>) {
        this.toDoList.addAll(toDoList)
    }

    override suspend fun updateToDoItem(toDoEntity: ToDoEntity): Boolean {
        val foundToDoEntity = toDoList.find { it.id == toDoEntity.id }
        return if (foundToDoEntity == null) {
            false
        } else {
            this.toDoList[toDoList.indexOf(foundToDoEntity)] = toDoEntity
            true
        }
    }

    override suspend fun getToDoItem(itemId: Long): ToDoEntity? {
        return toDoList.find { it.id == itemId }
    }

    override suspend fun deleteAll() {
        toDoList.clear()
    }

    override suspend fun deleteToDoItem(itemId: Long): Boolean {
        val foundToDoEntity = toDoList.find { it.id == itemId }
        return if (foundToDoEntity == null) {
            false
        } else {
            this.toDoList.removeAt(toDoList.indexOf(foundToDoEntity))
            true
        }
    }

}
<template>
    <Todo filter="active"/>
</template>

<script>
import Todo from '@/components/Todo.vue'

export default {
  name: 'active',
  components: {
    Todo
  }
}
</script>

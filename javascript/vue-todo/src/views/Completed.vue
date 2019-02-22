<template>
    <Todo filter="completed"/>
</template>

<script>
import Todo from '@/components/Todo.vue'

export default {
  name: 'completed',
  components: {
    Todo
  }
}
</script>

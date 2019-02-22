<template>
    <div>
    <section class='todoapp'>
      <header id='header'>
        <h1>todos</h1>
        <input class="new-todo" v-model="newTodo" placeholder="What needs to be done?" @keyup.enter="addTodo">
      </header>

      <section class='main'>
        <input id="toggle-all" class="toggle-all" @change="toggleCompleteAll" type="checkbox" />
        <label for="toggle-all"></label>
        <ul class="todo-list" v-for="todo in filteredTodos">
            <li class="todo" v-bind:class="{ completed: todo.complete, editing: todo.editing }">
                <input type="text" class="edit" v-model="todo.name" @keyup.enter="toggleEdit(todo)" v-if="todo.editing" />
                <div class="view" v-else>
                    <input type="checkbox" class="toggle" v-model="todo.complete" />
                    <label @dblclick="toggleEdit(todo)">{{todo.name}}</label>
                    <button @click="removeTodo(todo)" class="destroy"></button>
                </div>
            </li>
        </ul>
      </section>

      <footer class='footer'>
        <span class='todo-count' v-show="remaining">
          <strong v-text="remaining"></strong> {{pluralize('item', remaining)}} left
        </span>

        <ul class='filters'>
          <li><router-link to="/" active-class="selected" exact>All</router-link></li>
          <li><router-link to="/active" active-class="selected">Active</router-link></li>
          <li><router-link to="/completed" active-class="selected">Completed</router-link></li>
        </ul>

          <button class='clear-completed' v-show="remaining < todos.length" @click="clearCompleted">
            Clear completed
          </button>
      </footer>
    </section>

    <footer class='info'>
      <p>Double-click to edit a todo</p>
    </footer>
</div>

</template>

<script>
export default {
  name: 'Todo',
  props: ['filter'],
  data() {
    return {todos: [], newTodo: ''}
  },
  computed: {
    remaining() {
        return this.todos.filter(i => !i.complete).length;
    },
    filteredTodos() {
        const filters = {
            all: () => true,
            active: (t) => !t.complete,
            completed: (t) => t.complete
        };
        return this.todos.filter(t => filters[this.filter](t));
    }
  },
  methods: {
    addTodo() {
      this.todos.push({name: this.newTodo, complete: false, editing: false});
      this.newTodo = '';
    },
    removeTodo(todo) {
        const filteredTodos = this.todos.filter(i => i.name !== todo.name);
        this.todos = filteredTodos;
    },
    toggleTodoComplete(todo) {
        todo.complete = !todo.complete;
    },
    toggleCompleteAll() {
        this.todos.forEach(t => this.toggleTodoComplete(t));
    },
    clearCompleted() {
        this.todos = this.todos.filter(i => !i.complete);
    },
    toggleEdit(todo) {
        todo.editing = !todo.editing;
    },
    pluralize(word, count) {
        return `${word}${count > 1 ? 's' : ''}`;
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>

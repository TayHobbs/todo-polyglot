import Ember from 'ember';

export default Ember.Controller.extend({
  remaining: function() {
    return this.model.filterBy('completed', false).get('length');
  }.property('model.@each.completed'),

  actions: {
    createTodo: function() {
      var newTodoName = this.get('name');
      if (!newTodoName.trim()) { return; }

      var todo = this.store.createRecord('todo',{
        name: newTodoName
      });

      this.set('name', '');

      todo.save();
    },
    deleteTodo: function(todo) {
      todo.destroyRecord();
    },
    editTodo: function(todo) {
      todo.toggleProperty('editing');
    },
    acceptChanges: function(todo) {
      console.log(todo);
      todo.save();
      console.log(todo);
      this.send('editTodo', todo);
    }
  }
});

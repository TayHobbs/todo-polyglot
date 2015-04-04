import Ember from 'ember';

export default Ember.Component.extend({
  filtered: Ember.computed('todos.@each.completed', 'filter', function() {
    var all    = this.get('todos');
    var filter = this.get('filter');

    if (filter === 'all') { return all; }

    return all.filterBy('completed', filter === 'completed');
  }),

  completed: Ember.computed.filterBy('todos', 'completed', true),
  active: Ember.computed.filterBy('todos', 'completed', false),

  inflection: Ember.computed('active.[]', function() {
    var active = this.get('active.length');
    return active === 1 ? 'item' : 'items';
  }).readOnly(),

  allAreDone: Ember.computed('filtered.@each.completed', function(key, value) {
    if (arguments.length === 2) {
      var todos = this.get('todos');
      todos.setEach('completed', value);
      todos.invoke('save');
    } else {
      return !Ember.isEmpty(this) && this.get('todos.length') === this.get('completed.length');
    }
  }),

  actions: {

    createTodo() {
      var name = this.get('newName');

      if (name && !name.trim()) {
        this.set('newName', '');
        return;
      }

      var todo = this.store.createRecord('todo',{
        name: name
      });

      this.set('newName', '');
      todo.save();
    },

    clearCompleted() {
      var completed = this.get('completed');
      completed.toArray().
        invoke('deleteRecord'),
        invoke('save');
    }
  }
});

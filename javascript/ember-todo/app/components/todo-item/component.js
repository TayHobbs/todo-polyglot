import Ember from 'ember';

export default Ember.Component.extend({
  tagName: 'li',
  classNameBindings: ['todo.completed:completed', 'isEditing:editing'],

  init() {
    this._super(...arguments);
    this.set('isEditing', false);
  },

  actions: {
    editTodo() {
      this.set('isEditing', true);
    },

    removeTodo() {
      this.get('todo').destroyRecord();
    },

    save() {
      this.set('isEditing', false);
      this.get('todo').save();
    }
  }
});

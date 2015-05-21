/*jshint quotmark:false */
/*jshint white:false */
/*jshint trailing:false */
/*jshint newcap:false */
var app = app || {};

(function() {
  'use strict';
  var Utils = app.Utils;

  app.TodoModel = function(key) {
    this.key       = key;
    this.todos     = Utils.store(key);
    this.onChanges = [];
  };

  app.TodoModel.prototype.inform = function() {
    Utils.store(this.key, this.todos);
    this.onChanges.forEach(function(cb) { cb(); });
  };

  app.TodoModel.prototype.addTodo = function(title) {
    this.todos = this.todos.concat({
      id: Utils.uuid(),
      title: title,
      completed: false
    });
    this.inform();
  };

  app.TodoModel.prototype.toggleAll = function(checked) {
    this.todos = this.todos.map(function(todo) {
      return Utils.extend({}, todo, { completed: checked });
    });
    this.inform();
  };

  app.TodoModel.prototype.toggle = function(todoToToggle) {
    this.todos = this.todos.map(function(todo) {
      return todo !== todoToToggle ? todo : Utils.extend({}, todo, { completed: !todo.completed });
    });
    this.inform();
  };

  app.TodoModel.prototype.destroy = function(todo) {
    this.todos = this.todos.filter(function(candidate) {
      return candidate !== todo;
    });
  };

  app.TodoModel.prototype.save = function(todoToSave, text) {
    this.todos = this.todos.map(function(todo) {
      return todo !== todoToSave ? todo : Utils.extend({}, todo, { title: text });
    });
    this.inform();
  };

  app.TodoModel.prototype.clearCompleted = function() {
    this.todos = this.todos.filter(function(todo) {
      return !todo.completed;
    });
    this.inform();
  };
})();

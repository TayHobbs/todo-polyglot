/**
 * TodoController
 *
 * @description :: Server-side logic for managing Todoes
 * @help        :: See http://links.sailsjs.org/docs/controllers
 */

module.exports = {

  index: function(req, res) {
    Todo.find(function(err, todos) {
      return res.view({ todos: todos });
    });
  },

  completed: function(req, res) {
    Todo.find({ where: { completed: true }}, function(err, todos) {
      return res.view({ todos: todos });
    });
  },

  active: function(req, res) {
    Todo.find({ where: { completed: null }}, function(err, todos) {
      return res.view({ todos: todos });
    });
  },

  create: function(req, res) {
    Todo.create({ name: req.body.todo }).exec(function createCB(err, created) {
      console.log('Created todo with name ' + created.name);
    });
    return res.redirect('/todo/index');
  },

  update_name: function(req, res) {
    Todo.update({ id: req.body.id }, { name: req.body.todo }).exec(function afterwards(err, updated) {});
    return res.redirect('/todo/index');
  },

  update_completed: function(req, res) {
    Todo.update({ id: req.body.id }, { completed: req.body.completed }).exec(function afterwards(err, updated) {});
    return res.redirect('/todo/index');
  },

  destroy: function(req, res) {
    Todo.destroy({ id: req.body.id }).exec(function deleteCB(err, deleted) {
      console.log('Deleted todo with name ' + deleted.name);
    });
    return res.redirect('/todo/index');
  },

  clear_completed: function(req, res) {
    Todo.find({ where: { completed: true }}, function(err, todos) {
      _.forEach(todos, function(todo) {
        Todo.destroy({ id: todo.id }).exec(function deleteCB(err, deleted) {});
      });
    });
    return res.redirect('/todo/index');
  }

};

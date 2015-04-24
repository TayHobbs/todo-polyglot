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

  add_todo: function(req, res) {
    Todo.create({ name: req.body.todo }).exec(function createCB(err, created) {
      console.log('Created todo with name ' + created.name);
    });
    return res.redirect('/todo/index');
  }

};

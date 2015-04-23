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
  }

};

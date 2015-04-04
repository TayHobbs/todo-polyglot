import DS from 'ember-data';

var Todo = DS.Model.extend({
  name:      DS.attr('string'),
  completed: DS.attr('boolean', { defaultValue: false })
});

Todo.reopenClass({
  FIXTURES: [
    {
      id: 1,
      name: 'Todo 1',
      completed: false
    }
  ]
});

export default Todo;

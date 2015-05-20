var data = [];

var TodoList = React.createClass({
  handleSubmit: function(todo) {
    data.push(todo);
    this.setState({ data: data });
  },
  render: function() {
    return (
      <div className='todo-list'>
        <h1>Todos!</h1>
        <CurrentTodos data={this.props.data} />
        <NewTodo TodoSubmit={this.handleSubmit} />
      </div>
    );
  }
});
var CurrentTodos = React.createClass({
  render: function() {
    var todoNodes = this.props.data.map(function (todo) {
      return (
        <Todo>
          {todo.name}
        </Todo>
      );
    });
    return (
      <div className="todo-list">
        {todoNodes}
      </div>
    );
  }
});

var NewTodo = React.createClass({
  handleSubmit: function(e) {
    e.preventDefault();
    var name = React.findDOMNode(this.refs.name).value.trim();
    if (!name) {
      return;
    }
    this.props.TodoSubmit({ name: name });
    React.findDOMNode(this.refs.name).value = '';
    return;
  },
  render: function() {
    return (
      <form className="new-todo" onSubmit={this.handleSubmit}>

        <input type="text" placeholder="Your name"  ref="name"/>
        <input type="submit" value="Post" />
      </form>
    );
  }
});
var Todo = React.createClass({
  render: function() {
    return (
      <div className="todo">
        {this.props.children}
      </div>
    );
  }
});

React.render(
  <TodoList data={data} />,
  document.getElementById('todoapp')
);


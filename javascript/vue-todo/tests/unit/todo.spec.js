import { expect } from 'chai';
import { shallowMount } from '@vue/test-utils';
import Todo from '@/components/Todo.vue';

describe('Todo.vue', () => {
  it('renders with empty state', () => {
    const wrapper = shallowMount(Todo, {});
    expect(wrapper.find('.main').text()).to.equal('');
  });

  it('renders list of todos', () => {
    const wrapper = shallowMount(Todo, {});
    wrapper.vm.$data.todos.push({name: 'Wash Dishes'});
    expect(wrapper.find('.main').text()).to.equal('Wash Dishes');
  });

  it('addTodo method pushes newTodo to todos and clears input', () => {
    const wrapper = shallowMount(Todo, {});
    wrapper.vm.$data.newTodo = 'Wash Dishes';
    wrapper.vm.addTodo();
    expect(wrapper.find('.main').text()).to.equal('Wash Dishes');
    expect(wrapper.vm.$data.newTodo).to.equal('');
  });

  it('toggleCompleteTodo method changes todo to complete', () => {
    const wrapper = shallowMount(Todo, {});
    wrapper.setData({todos: [{name: 'Wash Dishes'}]});
    wrapper.vm.toggleTodoComplete(wrapper.vm.$data.todos[0]);
    expect(wrapper.vm.$data.todos[0].complete).to.be.true;
  });

  it('complete todos have correct class', () => {
    const wrapper = shallowMount(Todo, {});
    wrapper.setData({todos: [{name: 'Wash Dishes', complete: true}]});
    expect(wrapper.find('.completed').exists()).to.be.true;
  });

  it('can delete todo', () => {
    const wrapper = shallowMount(Todo, {});
    wrapper.vm.$data.todos.push({name: 'Wash Dishes'});
    wrapper.vm.removeTodo({name: 'Wash Dishes'});
    expect(wrapper.find('.todo').exists()).to.be.false;
  });

  it('can complete all todos', () => {
    const wrapper = shallowMount(Todo, {});
    wrapper.setData({todos: [
      {name: 'Mow Lawn', complete: false},
      {name: 'Wash Dishes', complete: false}]});
    wrapper.vm.toggleCompleteAll();
    expect(wrapper.vm.$data.todos[0].complete).to.be.true;
    expect(wrapper.vm.$data.todos[1].complete).to.be.true;
  });

  it('can clear all completed todos', () => {
    const wrapper = shallowMount(Todo, {});
    wrapper.setData({todos: [
      {name: 'Mow Lawn', complete: true},
      {name: 'Vacuum', complete: false},
      {name: 'Wash Dishes', complete: true}]});
    wrapper.vm.clearCompleted();
    expect(wrapper.vm.$data.todos.length).to.equal(1)
  });

  it('remaining returns number of incomplete todos', () => {
    const wrapper = shallowMount(Todo, {});
    wrapper.setData({todos: [
      {name: 'Mow Lawn', complete: true},
      {name: 'Vacuum', complete: false},
      {name: 'Wash Dishes', complete: true}]});
    expect(wrapper.vm.remaining).to.equal(1)
  });

  it('pluralize adds s to word if count if greater than 1', () => {
    const wrapper = shallowMount(Todo, {});
    expect(wrapper.vm.pluralize('item', 2)).to.equal('items')
  });

  it('pluralize does not add s to word if count if less than or equal to 1', () => {
    const wrapper = shallowMount(Todo, {});
    expect(wrapper.vm.pluralize('item', 1)).to.equal('item')
  });

  it('toggleEdit sets toggles editing', () => {
    const wrapper = shallowMount(Todo, {});
    wrapper.setData({todos: [{name: 'Mow Lawn', editing: false}]});
    wrapper.vm.editTodo(wrapper.vm.$data.todos[0]);
    expect(wrapper.vm.$data.todos[0].editing).to.be.true;
    wrapper.vm.editTodo(wrapper.vm.$data.todos[0]);
    expect(wrapper.vm.$data.todos[0].editing).to.be.false;
  });

  it('editing todo has correct todo', () => {
    const wrapper = shallowMount(Todo, {});
    wrapper.setData({todos: [{name: 'Mow Lawn', editing: true}]});
    expect(wrapper.find('.editing').exists()).to.be.true;
  });
});

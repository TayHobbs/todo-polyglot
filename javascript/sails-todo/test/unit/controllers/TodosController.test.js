var request = require('supertest');

describe('UsersController', function() {

  describe('Index', function() {
    it('Should be able to hit index page', function (done) {
      request(sails.hooks.http.app)
        .get('/todo/index')
        .expect(200, done);
    });
  });

});

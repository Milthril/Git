function createOriginBox(world) {
  var bd = new b2.BodyDef();
  var body = world.CreateBody(bd);
  var fd = new b2.FixtureDef();
  fd.friction = 1;
  fd.shape = new b2.PolygonShape();

  // cabinet
  var edges = [
    new b2.Vec2(-0.3, -10),
    new b2.Vec2(-0.3, 0),
    new b2.Vec2(3.5, 0),
    new b2.Vec2(3.5,-10)
  ];

  fd.shape.Set(edges, edges.length);
  body.CreateFixture(fd);
  return body;
}

function createOriginFloor(world) {
  var bd = new b2.BodyDef();
  var body = world.CreateBody(bd);
  var fd = new b2.FixtureDef();
  fd.friction = 0.5;
  fd.shape = new b2.ChainShape();

  // flat floor
  var edges = [
    new b2.Vec2(-2.9, 3),
    new b2.Vec2(-2.9, -10),
    new b2.Vec2(10,-10)
  ];

  fd.shape.CreateChain(edges, edges.length);
  body.CreateFixture(fd);
  return body;
}

function createTargetFloor(world) {
  var bd = new b2.BodyDef();
  var body = world.CreateBody(bd);
  var fd = new b2.FixtureDef();
  fd.friction = 1;
  fd.shape = new b2.PolygonShape();

  // flat floor
  var edges = [
    new b2.Vec2(7, -1),
    new b2.Vec2(7, 0),
    new b2.Vec2(15, 0),
    new b2.Vec2(15, -1)
  ];

  fd.shape.Set(edges, edges.length);
  body.CreateFixture(fd);
  return body;
}

function createTrashBin(world) {
  var bd = new b2.BodyDef();
  var fd = new b2.FixtureDef();

  bd.type = b2.Body.b2_dynamicBody;
  bd.linearDamping = 0;
  bd.angularDamping = 0.01;
  bd.allowSleep = true;
  bd.awake = true;

  fd.density = 0.1;

  var trashbin = world.CreateBody(bd);

  var shape1 = [
    new b2.Vec2(4.1, -7.5),
    new b2.Vec2(4.2, -7.5),
    new b2.Vec2(4.5, -9.9),
    new b2.Vec2(4.6, -9.9)
  ];

  var shape2 = [
    new b2.Vec2(4.5, -9.8),
    new b2.Vec2(4.5, -9.9),
    new b2.Vec2(5.7, -9.9),
    new b2.Vec2(5.7, -9.8)
  ];

  var shape3 = [
    new b2.Vec2(6.1, -7.5),
    new b2.Vec2(6.0, -7.5),
    new b2.Vec2(5.7, -9.9),
    new b2.Vec2(5.6, -9.9)
  ];

  fd.shape = new b2.PolygonShape();
  fd.shape.Set(shape1, shape1.length);
  trashbin.CreateFixture(fd);

  fd.shape = new b2.PolygonShape();
  fd.shape.Set(shape2, shape2.length);
  trashbin.CreateFixture(fd);

  fd.shape = new b2.PolygonShape();
  fd.shape.Set(shape3, shape3.length);

  trashbin.CreateFixture(fd);

  return trashbin;
}
var Cat = function() {
  this.__constructor.apply(this, arguments);
}

Cat.prototype.__constructor = function(world, genome) {

  this.world = world;

  this.max_x = 0;
  this.max_y = 0;
  this.max_score = 0;

  this.density = 25; // common for all fixtures, no reason to be too specific

  this.bd = new b2.BodyDef();
  this.bd.type = b2.Body.b2_dynamicBody;
  this.bd.linearDamping = 0;
  this.bd.angularDamping = 0.01;
  this.bd.allowSleep = true;
  this.bd.awake = true;

  this.fd = new b2.FixtureDef();
  this.fd.density = this.density;
  this.fd.restitution = 0.1;
  this.fd.shape = new b2.PolygonShape();
  this.fd.filter.groupIndex = -1;
  this.fd.friction = 0.7;

  this.bodies = [];
  this.bodies.push(this.front_left_leg_top = this.createFrontLegTop());
  this.bodies.push(this.front_left_leg_middle = this.createFrontLegMiddle());
  this.bodies.push(this.front_left_leg_low = this.createFrontLegLow());
  this.bodies.push(this.front_left_leg_toe = this.createFrontLegToe());

  this.bodies.push(this.back_left_leg_top = this.createBackLegTop());
  this.bodies.push(this.back_left_leg_middle = this.createBackLegMiddle());
  this.bodies.push(this.back_left_leg_low = this.createBackLegLow());
  this.bodies.push(this.back_left_leg_toe = this.createBackLegToe());

  this.bodies.push(this.tail_1 = this.createTail1());
  this.bodies.push(this.tail_2 = this.createTail2());
  this.bodies.push(this.tail_3 = this.createTail3());
  this.bodies.push(this.tail_4 = this.createTail4());
  this.bodies.push(this.tail_5 = this.createTail5());

  this.bodies.push(this.neck = this.createNeck());
  this.bodies.push(this.head = this.createHead());
  this.bodies.push(this.lower_torso = this.createLowerTorso());
  this.bodies.push(this.upper_torso = this.createUpperTorso());

  this.bodies.push(this.front_right_leg_toe = this.createFrontLegToe());
  this.bodies.push(this.front_right_leg_low = this.createFrontLegLow());
  this.bodies.push(this.front_right_leg_middle = this.createFrontLegMiddle());
  this.bodies.push(this.front_right_leg_top = this.createFrontLegTop());

  this.bodies.push(this.back_right_leg_toe = this.createBackLegToe());
  this.bodies.push(this.back_right_leg_low = this.createBackLegLow());
  this.bodies.push(this.back_right_leg_middle = this.createBackLegMiddle());
  this.bodies.push(this.back_right_leg_top = this.createBackLegTop());

  this.connectParts();

  this.genome = this.createGenome(genome);
}

Cat.prototype.createFixturedBody = function(position, coords) {
  this.bd.position.Set(position.x, position.y);
  var body = this.world.CreateBody(this.bd);

  this.fd.shape.Set(coords, coords.length);
  body.CreateFixture(this.fd);

  return body;
}

Cat.prototype.createHead = function() {
  var position = new b2.Vec2(3.9, 2.2);
  var coords = [
    new b2.Vec2(-0.057, 0.314),
    new b2.Vec2(-0.371, 0.137),
    new b2.Vec2(-0.222, -0.245),
    new b2.Vec2(0.182, -0.479),
    new b2.Vec2(0.399, -0.245),
    new b2.Vec2(0.371, 0.017)
  ];
  return this.createFixturedBody(position, coords);
}

Cat.prototype.createNeck = function() {
  var position = new b2.Vec2(3.347, 2);
  var coords = [
    new b2.Vec2(0.18, 0.36),
    new b2.Vec2(-0.25, 0.16),
    new b2.Vec2(-0.3, -0.2),
    new b2.Vec2(-0.08, -0.23),
    new b2.Vec2(0.3, 0)
  ];
  return this.createFixturedBody(position, coords);
}

Cat.prototype.createUpperTorso = function() {
  var position = new b2.Vec2(2.4, 1.8);
  var coords = [
    new b2.Vec2(-0.71, 0.5),
    new b2.Vec2(-0.73, -0.01),
    new b2.Vec2(-0.67, -0.26),
    new b2.Vec2(0.63, -0.33),
    new b2.Vec2(0.72, 0.36)
  ];
  this.fd.density = this.density/2;
  var body = this.createFixturedBody(position, coords);
  this.fd.density = this.density;
  return body;
}

Cat.prototype.createLowerTorso = function() {
  var position = new b2.Vec2(1.2, 2.1);
  var coords = [
    new b2.Vec2(0.5, 0.2),
    new b2.Vec2(-0.3, 0.3),
    new b2.Vec2(-0.7, 0),
    new b2.Vec2(-0.67, -0.48),
    new b2.Vec2(0.5, -0.5)
  ];
  return this.createFixturedBody(position, coords);
}

Cat.prototype.createFrontLegTop = function() {
  var position = new b2.Vec2(2.8, 1.4);
  var coords = [
    new b2.Vec2(0.3, 0.6),
    new b2.Vec2(-0.1, 0.6),
    new b2.Vec2(-0.4, 0),
    new b2.Vec2(-0.1, -0.4),
    new b2.Vec2(0.4, 0)
  ];
  return this.createFixturedBody(position, coords);
}

Cat.prototype.createFrontLegMiddle = function() {
  var position = new b2.Vec2(2.55, 0.87);
  var coords = [
    new b2.Vec2(-0.05, 0.42),
    new b2.Vec2(-0.23, 0.26),
    new b2.Vec2(-0.1, -0.44),
    new b2.Vec2(0.17, -0.41),
    new b2.Vec2(0.2, 0.17)
  ];
  return this.createFixturedBody(position, coords);
}

Cat.prototype.createFrontLegLow = function() {
  var position = new b2.Vec2(2.6, 0.3);
  var coords = [
    new b2.Vec2(0.08, 0.16),
    new b2.Vec2(-0.15, 0.14),
    new b2.Vec2(-0.05, -0.2),
    new b2.Vec2(0.13, -0.1)
  ];
  return this.createFixturedBody(position, coords);
}

Cat.prototype.createFrontLegToe = function() {
  var position = new b2.Vec2(2.8, 0.1);
  var coords = [
    new b2.Vec2(0.1, 0.1),
    new b2.Vec2(-0.2, 0.1 ),
    new b2.Vec2(-0.2, -0.1),
    new b2.Vec2(0.1, -0.1)
  ];
  var default_friction = this.fd.friction;
  this.fd.friction = 1;
  var body = this.createFixturedBody(position, coords);
  this.fd.friction = default_friction;
  return body;
}

Cat.prototype.createBackLegTop = function() {
  var position = new b2.Vec2(0.8, 1.6);
  var coords = [
    new b2.Vec2(0, 0.5),
    new b2.Vec2(-0.4, 0.3),
    new b2.Vec2(-0.3, -0.3),
    new b2.Vec2(-0.2, -0.5),
    new b2.Vec2(0.38, -0.37),
    new b2.Vec2(0.47, -0.16),
    new b2.Vec2(0.4, 0.2)
  ];
  return this.createFixturedBody(position, coords);
}

Cat.prototype.createBackLegMiddle = function() {
  var position = new b2.Vec2(0.8, 0.9);
  var coords = [
    new b2.Vec2(0.44, 0.34),
    new b2.Vec2(-0.1, 0.3),
    new b2.Vec2(-0.3, -0.2),
    new b2.Vec2(-0.1, -0.4)
  ];
  return this.createFixturedBody(position, coords);
}

Cat.prototype.createBackLegLow = function() {
  var position = new b2.Vec2(0.8, 0.4);
  var coords = [
    new b2.Vec2(-0.08, 0.24),
    new b2.Vec2(-0.25, 0.12),
    new b2.Vec2(0.15, -0.27),
    new b2.Vec2(0.26, -0.13)
  ];
  return this.createFixturedBody(position, coords);
}

Cat.prototype.createBackLegToe = function() {
  var position = new b2.Vec2(1.13, 0.14);
  var coords = [
    new b2.Vec2(-0.16, 0.2),
    new b2.Vec2(-0.16, 0),
    new b2.Vec2(0.15, 0),
    new b2.Vec2(0.15, 0.2)
  ];
  var default_friction = this.fd.friction;
  this.fd.friction = 1;
  var body = this.createFixturedBody(position, coords);
  this.fd.friction = default_friction;
  return body;
}

Cat.prototype.createTail1 = function() {
  var position = new b2.Vec2(0.26, 1.96);
  var coords = [
    new b2.Vec2(0.18, 0.18),
    new b2.Vec2(-0.26, -0.08),
    new b2.Vec2(-0.19, -0.22),
    new b2.Vec2(0.28, 0.04)
  ];
  return this.createFixturedBody(position, coords);
}

Cat.prototype.createTail2 = function() {
  var position = new b2.Vec2(-0.16, 1.75);
  var coords = [
    new b2.Vec2(0.18, 0.15),
    new b2.Vec2(-0.23, -0.02),
    new b2.Vec2(-0.19, -0.17),
    new b2.Vec2(0.23, 0)
  ];
  return this.createFixturedBody(position, coords);
}

Cat.prototype.createTail3 = function() {
  var position = new b2.Vec2(-0.59, 1.7);
  var coords = [
    new b2.Vec2(-0.18, 0.13),
    new b2.Vec2(-0.25, 0.02),
    new b2.Vec2(0.18, -0.11),
    new b2.Vec2(0.22, 0.03)
  ];
  return this.createFixturedBody(position, coords);
}

Cat.prototype.createTail4 = function() {
  var position = new b2.Vec2(-0.95, 1.89);
  var coords = [
    new b2.Vec2(-0.08, 0.12),
    new b2.Vec2(-0.16, 0.04),
    new b2.Vec2(0.11, -0.14),
    new b2.Vec2(0.17, -0.03)
  ];
  return this.createFixturedBody(position, coords);
}

Cat.prototype.createTail5 = function() {
  var position = new b2.Vec2(-1.18, 2.12);
  var coords = [
    new b2.Vec2(-0.04, 0.13),
    new b2.Vec2(-0.12, 0.06),
    new b2.Vec2(0.08, -0.19),
    new b2.Vec2(0.13, -0.10)
  ];
  return this.createFixturedBody(position, coords);
}

Cat.prototype.createJoint = function(joint_data) {
  var jd = new b2.RevoluteJointDef();
  jd.Initialize(joint_data.bodyA, joint_data.bodyB, {x:joint_data.positionX, y:joint_data.positionY});
  jd.lowerAngle = joint_data.lowerAngle;
  jd.upperAngle = joint_data.upperAngle;
  jd.enableLimit = true;
  jd.maxMotorTorque = joint_data.maxTorque;
  jd.motorSpeed = 0;
  jd.enableMotor = true;
  var joint = this.world.CreateJoint(jd);
  if(joint_data.gene)
    this.joints.push(joint);
}

Cat.prototype.connectParts = function() {
  this.joints = [];
  var joint_data_array = [
    {bodyA:this.neck,                   bodyB:this.head,                    positionX:3.5, positionY:2.5, lowerAngle:-Math.PI/12, upperAngle:Math.PI/12,  maxTorque:300},
    {bodyA:this.upper_torso,            bodyB:this.neck,                    positionX:3.1, positionY:2.1, lowerAngle:-Math.PI/6,  upperAngle:Math.PI/18, maxTorque:500},
    {gene:true, bodyA:this.lower_torso,            bodyB:this.upper_torso,             positionX:1.7, positionY:2.2, lowerAngle:-Math.PI/6,  upperAngle:Math.PI/12,           maxTorque:1000},

    {gene:true, bodyA:this.upper_torso,            bodyB:this.front_right_leg_top,     positionX:2.9,  positionY:1.9, lowerAngle:-Math.PI/3,  upperAngle:Math.PI/4,   maxTorque:100},
    {gene:true, bodyA:this.front_right_leg_top,    bodyB:this.front_right_leg_middle,  positionX:2.5, positionY:1.2, lowerAngle:-Math.PI/18, upperAngle:Math.PI/3,   maxTorque:700},
    {gene:true, bodyA:this.front_right_leg_middle, bodyB:this.front_right_leg_low,     positionX:2.5, positionY:0.4, lowerAngle:-Math.PI/2.5,  upperAngle:0,  maxTorque:400},
    {gene:true, bodyA:this.front_right_leg_low,    bodyB:this.front_right_leg_toe,     positionX:2.65, positionY:0.1, lowerAngle:-Math.PI/2, upperAngle:0,  maxTorque:300},

    {gene:true, bodyA:this.upper_torso,            bodyB:this.front_left_leg_top,      positionX:2.9,  positionY:1.9, lowerAngle:-Math.PI/3,  upperAngle:Math.PI/4,   maxTorque:100},
    {gene:true, bodyA:this.front_left_leg_top,     bodyB:this.front_left_leg_middle,   positionX:2.5, positionY:1.2, lowerAngle:-Math.PI/18, upperAngle:Math.PI/3,   maxTorque:700},
    {gene:true, bodyA:this.front_left_leg_middle,  bodyB:this.front_left_leg_low,      positionX:2.5, positionY:0.4, lowerAngle:-Math.PI/2.5,  upperAngle:0,  maxTorque:400},
    {gene:true, bodyA:this.front_left_leg_low,     bodyB:this.front_left_leg_toe,      positionX:2.65, positionY:0.1, lowerAngle:-Math.PI/2, upperAngle:0,  maxTorque:300},

    {gene:true, bodyA:this.lower_torso,            bodyB:this.back_right_leg_top,      positionX:0.7, positionY:2,  lowerAngle:-Math.PI/3,  upperAngle:Math.PI/6,   maxTorque:1200},
    {gene:true, bodyA:this.back_right_leg_top,     bodyB:this.back_right_leg_middle,   positionX:1,  positionY:1.2, lowerAngle:-Math.PI/3,  upperAngle:Math.PI/7,  maxTorque:800},
    {gene:true, bodyA:this.back_right_leg_middle,  bodyB:this.back_right_leg_low,      positionX:0.6, positionY:0.6, lowerAngle:-Math.PI/4, upperAngle:Math.PI/9,   maxTorque:400},
    {gene:true, bodyA:this.back_right_leg_low,     bodyB:this.back_right_leg_toe,      positionX:0.95,  positionY:0.1, lowerAngle:-Math.PI/6, upperAngle:0,  maxTorque:200},

    {gene:true, bodyA:this.lower_torso,            bodyB:this.back_left_leg_top,       positionX:0.7, positionY:2,  lowerAngle:-Math.PI/3,  upperAngle:Math.PI/6,   maxTorque:1200},
    {gene:true, bodyA:this.back_left_leg_top,      bodyB:this.back_left_leg_middle,    positionX:1,  positionY:1.2, lowerAngle:-Math.PI/3,  upperAngle:Math.PI/7,  maxTorque:800},
    {gene:true, bodyA:this.back_left_leg_middle,   bodyB:this.back_left_leg_low,       positionX:0.6, positionY:0.6, lowerAngle:-Math.PI/4, upperAngle:Math.PI/9,   maxTorque:400},
    {gene:true, bodyA:this.back_left_leg_low,      bodyB:this.back_left_leg_toe,       positionX:0.95,  positionY:0.1, lowerAngle:-Math.PI/6, upperAngle:0,  maxTorque:200},

    {bodyA:this.lower_torso,            bodyB:this.tail_1,                  positionX:0.49, positionY:2.13, lowerAngle:-Math.PI/1.5, upperAngle:Math.PI/12,  maxTorque:60},
    {bodyA:this.tail_1,                 bodyB:this.tail_2,                  positionX:0.04, positionY:1.83, lowerAngle:-Math.PI/12, upperAngle:Math.PI/12,  maxTorque:60},
    {bodyA:this.tail_2,                 bodyB:this.tail_3,                  positionX:-0.38, positionY:1.68, lowerAngle:-Math.PI/12, upperAngle:Math.PI/12,  maxTorque:60},
    {bodyA:this.tail_3,                 bodyB:this.tail_4,                  positionX:-0.8, positionY:1.8, lowerAngle:-Math.PI/12, upperAngle:Math.PI/12,  maxTorque:60},
    {bodyA:this.tail_4,                 bodyB:this.tail_5,                  positionX:-1.08, positionY:1.98, lowerAngle:-Math.PI/12, upperAngle:Math.PI/12,  maxTorque:60}
  ];

  for(var k = 0; k < joint_data_array.length; k++) {
    this.createJoint(joint_data_array[k]);
  }
}

Cat.prototype.randomChromossome = function() {
  var chromossome = {
    time_factor: Math.random()/10,
    time_shift: Math.random()*Math.PI/2,
    cos_factor: 50*Math.random() - 25
  };
  return chromossome
}

Cat.prototype.createGenome = function(genome) {
  if(typeof genome == 'undefined' || genome == null) {
    var genome = [];
    for(var k = 0; k < this.joints.length; k++) {
      genome.push(this.randomChromossome());
    }
  }
  return genome;
}

Cat.prototype.simulationStep = function(framecounter) {
  for(var k = 0; k < this.joints.length; k++) {
    this.joints[k].SetMotorSpeed( this.genome[k].cos_factor*Math.cos(this.genome[k].time_factor*framecounter + this.genome[k].time_shift) );
  }

  var pos = this.upper_torso.GetPosition();

  this.x = pos.x - 2.4;
  this.y = pos.y - 1.8;
  this.max_x = Math.max(this.max_x, this.x);
  this.max_y = Math.max(this.max_y, this.y);
  if(this.x > 0 && this.y > 0) {
    this.max_score = Math.max(this.max_score, Math.sqrt(Math.pow(this.x,2) + Math.pow(this.y,2)));
  }
}
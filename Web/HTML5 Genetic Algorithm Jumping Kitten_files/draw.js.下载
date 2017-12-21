drawInit = function() {
  globals.main_screen = document.getElementById("main_screen");
  globals.ctx = main_screen.getContext("2d");
  resetCamera();
}

resetCamera = function() {
  globals.zoom = config.max_zoom_factor;
  globals.translate_x = 3;
  globals.translate_y = 180;
}

drawFrame = function() {
  globals.ctx.clearRect(0, 0, globals.main_screen.width, globals.main_screen.height);
  globals.ctx.save();
  globals.ctx.translate(globals.translate_x*globals.zoom, globals.translate_y);
  globals.ctx.scale(globals.zoom, -globals.zoom);
  drawFloor(globals.origin_floor);
  drawTargetPlatform(globals.target_floor);
  drawCat(globals.cat);
  drawBin(globals.trashbin);
  drawCabinet(globals.cabinet);
  globals.ctx.restore();
}

drawShape = function(body) {
  // set strokestyle and fillstyle before call
  globals.ctx.beginPath();
  var fixture = body.GetFixtureList();
  do {
    var shape = fixture.GetShape();
    var p0 = body.GetWorldPoint(shape.m_vertices[0]);
    globals.ctx.moveTo(p0.x, p0.y);
    for(var k = 1; k < shape.m_vertices.length; k++) {
      if(!shape.m_vertices[k]) {
        break;
      }
      var p = body.GetWorldPoint(shape.m_vertices[k]);
      globals.ctx.lineTo(p.x, p.y);
    }
    globals.ctx.lineTo(p0.x, p0.y);

    globals.ctx.fill();
    globals.ctx.stroke();
  } while (fixture = fixture.GetNext());
}


drawCat = function(cat) {
  globals.ctx.strokeStyle = "#9d5107";
  globals.ctx.fillStyle = "#e49c61";
  globals.ctx.lineWidth = 1/globals.zoom;

  for(var k = 0; k < cat.bodies.length; k++) {
    drawShape(cat.bodies[k]);
  }
}

drawBin = function(bin) {
  globals.ctx.strokeStyle = "#3f3f3f";
  globals.ctx.fillStyle = "#9f9f9f";
  globals.ctx.lineWidth = 1/globals.zoom;
  drawShape(bin);
}

drawCabinet = function(body) {
  globals.ctx.strokeStyle = "#3f3f3f";
  globals.ctx.fillStyle = "rgba(255,0,0,0.5)";
  globals.ctx.lineWidth = 1/globals.zoom;
  drawShape(body);
}

drawTargetPlatform = function(body) {
  globals.ctx.strokeStyle = "#3f3f3f";
  globals.ctx.fillStyle = "rgba(255,0,0,0.5)";
  globals.ctx.lineWidth = 1/globals.zoom;
  drawShape(body);
}

drawFloor = function(floor) {
  globals.ctx.strokeStyle = "#444";
  globals.ctx.lineWidth = 1/globals.zoom;
  globals.ctx.beginPath();
  var floor_fixture = floor.GetFixtureList();
  globals.ctx.moveTo(floor_fixture.m_shape.m_vertices[0].x, floor_fixture.m_shape.m_vertices[0].y);
  for(var k = 1; k < floor_fixture.m_shape.m_vertices.length; k++) {
    globals.ctx.lineTo(floor_fixture.m_shape.m_vertices[k].x, floor_fixture.m_shape.m_vertices[k].y);
  }
  globals.ctx.stroke();
}

drawTest = function() {
  globals.ctx.strokeStyle = "#000";
  globals.ctx.fillStyle = "#666";
  globals.ctx.lineWidth = 1;
  globals.ctx.beginPath();
  globals.ctx.moveTo(0, 0);
  globals.ctx.lineTo(0, 2);
  globals.ctx.lineTo(2, 2);

  globals.ctx.fill();
  globals.ctx.stroke();

}
config = {
  time_step: 60,
  simulation_fps: 85,
  draw_fps: 60,
  velocity_iterations: 8,
  position_iterations: 3,
  max_zoom_factor: 35,
  frame_limit: 60*6,
  pool_size: 30,
  mutation_chance: 0.025,
  mutation_amount: 0.025
};

globals = {};

gameInit = function() {
  drawInit();

  globals.world = new b2.World(new b2.Vec2(0, -10));

  globals.origin_floor = createOriginFloor(globals.world);
  globals.target_floor = createTargetFloor(globals.world);

  globals.frame_counter = 0;
  globals.cat = new Cat(globals.world);
  globals.cat_counter = 1;

  globals.cabinet = createOriginBox(globals.world);
  globals.trashbin = createTrashBin(globals.world);

  globals.gene_pool = [];

  globals.simulation_interval = setInterval(simulationStep, Math.round(1000/config.simulation_fps));
  globals.draw_interval = setInterval(drawFrame, Math.round(1000/config.draw_fps));
}

simulationStep = function() {
  globals.world.Step(1/config.time_step, config.velocity_iterations, config.position_iterations);
  globals.world.ClearForces();
  globals.frame_counter++
  globals.cat.simulationStep(globals.frame_counter);09
  if(globals.frame_counter > config.frame_limit) {
    clearInterval(globals.simulation_interval);
    killCat(globals.cat);
    globals.cat_counter++;
    globals.cat = new Cat(globals.world, makeGenome());
    globals.frame_counter = 0;
    globals.simulation_interval = setInterval(simulationStep, Math.round(1000/config.simulation_fps));
  }
}

killCat = function(cat) {
  globals.gene_pool.push({cat_id: globals.cat_counter, score:cat.max_score, genome:JSON.parse(JSON.stringify(cat.genome)), stringed:JSON.stringify(cat.genome)});
  for(var k = 0; k < cat.bodies.length; k++) {
    globals.world.DestroyBody(cat.bodies[k]);
  }
}

makeGenome = function() {
  globals.gene_pool.sort(function(a,b) {
    return b.score - a.score;
  });

  if(globals.gene_pool.length > config.pool_size) {
    globals.gene_pool.pop();
  }

  if(globals.gene_pool[0].score != globals.prev_high_score) {
    globals.prev_high_score = globals.gene_pool[0].score;
    console.log(globals.gene_pool[0].score);
  }

  var parent_ids = [];
  var parents = [];
  for(var k = 0; k < globals.gene_pool.length && parents.length < 2; k++) {
    if(Math.random() < 1/(k+2)) {
      parent_ids.push(k);
      parents.push(globals.gene_pool[k].genome);
    }
  }

  while(parents.length < 2) {
    parent_ids.push('rand');
    parents.push(globals.cat.createGenome());
  }

  console.log("parents: "+ parent_ids[0] + " + " + parent_ids[1]);
  return copulate(parents);
}

copulate = function(parents) {
  do {
    var new_genome = [];
    var count_0 = 0;
    var count_1 = 0;
    var count_mut = 0;
    for(var k = 0; k < parents[0].length; k++) {
      if(Math.random() < 0.5) {
        new_genome.push(JSON.parse(JSON.stringify(parents[0][k])));
        count_0 += 3;
      } else {
        new_genome.push(JSON.parse(JSON.stringify(parents[1][k])));
        count_1 += 3;
      }

      for(var g in new_genome[k]) {
        if(Math.random() < config.mutation_chance) {
          new_genome[k][g] = new_genome[k][g] * (1+2*config.mutation_amount*Math.random()-config.mutation_amount);
          count_mut++;
        }
      }
    }
  } while (is_clone(new_genome));

  var total = count_0 + count_1;
  console.log("p0: "+Math.round(100*count_0/total)+"%");
  console.log("p1: "+Math.round(100*count_1/total)+"%");
  console.log("mutations: "+Math.round(100*count_mut/total)+"%");
  return new_genome;
}

is_clone = function(new_genome) {
  var stringed = JSON.stringify(new_genome);
  for(var k = 0; k < globals.gene_pool.length; k++) {
    if(stringed == globals.gene_pool[k].stringed) {
      console.log("### found clone ###");
      return true;
    }
  }
  return false;
}

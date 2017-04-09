var img;
var input, button, greeting;
var name = '.';
var R = 100,
    G = 100,
    B = 100;
var press_count = 0;
var max_press = 300;
var landscape_button, cat_button, cupcake_button;

function setup() {
    createCanvas(800, 600);
    img = loadImage("landscape2_lineart.png"); // Load an image into the program

    input = createInput();
    input.position(850, 65);
    button = createButton('submit');
    button.position(input.x + input.width, 65);
    button.mousePressed(names);
    greeting = createElement('h2', ':');
    greeting.position(850, 5);
    create_lineart_buttons();
    textAlign(CENTER);
    textSize(80);
}

function create_lineart_buttons() {
    landscape_button = createButton('color landscape');
    landscape_button.position(input.x, 65 + 40);
    landscape_button.mousePressed(load_landscape);
    cat_button = createButton('color cat');
    cat_button.position(input.x, 65 + 80);
    cat_button.mousePressed(load_cat);
    cupcake_button = createButton('color cupcake');
    cupcake_button.position(input.x, 65 + 120);
    cupcake_button.mousePressed(load_cupcake);
}

function names() {
    name = input.value();
    greeting.html(': ' + name);
    input.value('');
}

function draw() {
    image(img, 0, 0);

    if (mouseIsPressed) {
        fill(R + press_count * .2,
            G + press_count * .2,
            B + press_count * .5);
    } else {
        noFill();
    }
    noStroke();
    translate(mouseX, mouseY);
    text(name, 0, 0);
    if (press_count < max_press) {
        press_count++;
    } else {
        press_count = 0;
    }

    //ellipse(mouseX, mouseY, 80, 80);
}

function load_landscape() {
    background(color(255, 255, 255));
    img = loadImage("landscape2_lineart.png");
}

function load_cat() {
    background(color(255, 255, 255));
    img = loadImage("cat_lineart.png");
}

function load_cupcake() {
    background(color(255, 255, 255));
    img = loadImage("cupcake_lineart.png");
}

function keyTyped() {
    if (key == 'r') {
        R = 255;
        G = 50;
        B = 50;
    } else if (key == 'o') {
        R = 255;
        G = 181;
        B = 0;
    } else if (key == 'y') {
        R = 255;
        G = 246;
        B = 0;
    } else if (key == 'g') {
        R = 50;
        G = 255;
        B = 50;
    } else if (key == 'b') {
        R = 50;
        G = 50;
        B = 255;
    } else if (key == 'i') {
        R = 129;
        G = 16;
        B = 217;
    } else if (key == 'v') {
        R = 202;
        G = 16;
        B = 217;
    } else if (key == '0') {
        R = 100;
        G = 100;
        B = 100;
    }

}

//boss-------------------------------------------------

function Boss(){
	this.position = new Point();
	this.size = 0;
	this.life = 0;
	this.param = 0;
	this.alive = false;
}

Boss.prototype.set = function(p, size, life){
	//座標をセット
	this.position.x = p.x;
	this.position.y = p.y;

	//サイズ、耐久値をセット
	this.size = size;
	this.life = life;

	//パラメーターをセット
	this.param = 0;

	//生存フラグを立てる
	this.alive = true;
};

Boss.prototype.move = function(){
	var i, j;
	//パラメーターをインクリメント
	this.param++;


	//パラメータに応じて分岐
	switch(true){
		case this.param < 100:
			//下方向へまっすぐすすむ
			this.position.y += 1.5;
			break;
		default:
			//パラメータからradianを求める
			i = ((this.param - 100) % 360) * Math.PI / 180;

			//radianから横移動量を算出
			j = screenCanvas.width / 2;
			this.position.x = j + Math.sin(i) * j;
			break;
	}
};

//boss bit------------------------------------------------
function Bit(){
	this.position = new Point();
	this.parent = null;
	this.size = 0;
	this.life = 0;
	this.param = 0;
	this.alive = false;
}

Bit.prototype.set = function(parent, size, life, param){
	//母体となるボスをセット
	this.parent = parent;

	//サイズ・耐久値をセット
	this.size = size;
	this.life = life;

	//パラメーターに初期値をセット
	this.param = param;

	//生存フラグを立てる
	this.alive = true;
};

Bit.prototype.move = function(){
	var i, x, y;

	//パラメーターをインクリメント
	this.param++;

	//パラメーターからradianを求める
	i = (this.param % 360) * Math.PI / 180;

	//radianから横移動量を算出
	x = Math.cos(i) * (this.parent.size + this.size);
	y = Math.sin(i) * (this.parent.size + this.size);
	this.position.x = this.parent.position.x + x;
	this.position.y = this.parent.position.y + y;
};
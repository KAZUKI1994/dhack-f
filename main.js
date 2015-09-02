// global ------------------------
var screenCanvas, info;
var run = true;
var fps = 1000/30;
var mouse = new Point();
var ctx; //canvas2d context格納
var fire = false;
var counter = 0;
var score = 0;
var message = "";

// const--------------------------
var CHARA_COLOR = 'rgba(0, 0, 255, 0.75)';
var CHARA_SHOT_COLOR = 'rgba(0, 255, 0, 0.75)';
var CHARA_SHOT_MAX_COUNT = 10;
var ENEMY_COLOR = 'rgba(255, 0, 0, 0.75)';
var ENEMY_MAX_COUNT = 10;
var ENEMY_SHOT_COLOR = 'rgba(255, 0, 255, 0.75)';
var ENEMY_SHOT_MAX_COUNT = 100;
var BOSS_COLOR = 'rgba(128, 128, 128, 0.75)';
var BOSS_BIT_COLOR = 'rgba(64, 64, 64, 0.75)';
var BOSS_BIT_COUNT = 5;

// main --------------------------
window.onload = function(){

	var i, j;
	var p = new Point();

	//スクリーンの初期化
	screenCanvas = document.getElementById('screen');
	screenCanvas.width = 256;
	screenCanvas.height = 256;

	//2d context
	ctx = screenCanvas.getContext('2d');

	//イベント登録
	screenCanvas.addEventListener('mousemove', mouseMove, true);
	screenCanvas.addEventListener('mousedown', mouseDown, true);
	window.addEventListener('keydown', keyDown, true);

	//エレメント関連
	info = document.getElementById('info');

	//自機の初期化
	var chara = new Character();
	chara.init(10);

	//自機の初期位置を修正
	mouse.x = screenCanvas.width / 2;
	mouse.y = screenCanvas.height - 20;

	//ショットの初期化
	var charaShot = new Array(CHARA_SHOT_MAX_COUNT);
	for(i=0; i<CHARA_SHOT_MAX_COUNT; i++){
		charaShot[i] = new CharacterShot();
	}

	//敵の初期化
	var enemy = new Array(ENEMY_MAX_COUNT);
	for(i=0; i<ENEMY_MAX_COUNT; i++){
		enemy[i] = new Enemy();
	}

	//エネミーショットの初期化
	var enemyShot = new Array(ENEMY_SHOT_MAX_COUNT);
	for(i=0; i<ENEMY_SHOT_MAX_COUNT; i++){
		enemyShot[i] = new EnemyShot();
	}

	//ボスの初期化
	var boss = new Boss();

	//ボスのビットを初期化
	var bit = new Array(BOSS_BIT_COUNT);
	for(i=0; i<BOSS_BIT_COUNT; i++){
		bit[i] = new Bit();
	}

	//loop処理
	(function(){

		counter++;

		//HTMLを更新
		info.innerHTML = mouse.x + ' : ' + mouse.y;

		//screen clear
		ctx.clearRect(0, 0, screenCanvas.width, screenCanvas.height);

		//path setting start
		ctx.beginPath();


		//自機の位置を管理
		chara.position.x = mouse.x;
		chara.position.y = mouse.y;


		//set color of circle
		ctx.fillStyle = CHARA_COLOR;

		//set path to draw circle
		ctx.arc(chara.position.x, chara.position.y, chara.size, 0, Math.PI * 2, false);
		
		//draw circle
		ctx.fill();

		//fireフラグの値により分岐
		if(fire){	
			for(i=0; i<CHARA_SHOT_MAX_COUNT; i++){
				
				//自機ショットがすでに発射されているかチェック
				if(!charaShot[i].alive){
					//自機ショットを新規にセット
					charaShot[i].set(chara.position, 3, 5);

					//loopを抜ける
					break;
				}				
			}
			
			//フラグをおろしておく
			fire = false;
		}

		ctx.beginPath();
			//全ての自機ショットを調査する

		// すべての自機ショットを調査する
		for(i = 0; i < CHARA_SHOT_MAX_COUNT; i++){
 		   // 自機ショットが既に発射されているかチェック
    		if(charaShot[i].alive){
        		// 自機ショットを動かす
        		charaShot[i].move();

		        // 自機ショットを描くパスを設定
    		    ctx.arc(
        		    charaShot[i].position.x,
            		charaShot[i].position.y,
            		charaShot[i].size,
            		0, Math.PI * 2, false
        		);

	        	// パスをいったん閉じる
    	    	ctx.closePath();
    		}
		}

		// 自機ショットの色を描く
		ctx.fillStyle = CHARA_SHOT_COLOR;
		//自機ショットを描く
		ctx.fill();

		//エネミーの出現管理-------------------------------------
		if(counter%100 === 0 && counter < 1000){
			//全てのエネミーを調査する
			for(i=0; i<ENEMY_MAX_COUNT; i++){
				//エネミーの生存フラグをチェック
				if(!enemy[i].alive){
					//タイプをけっていするパラメーターを算出
					j = (counter % 200) / 100;

					//タイプに応じて初期値を決める
					var enemySize = 15;
					p.x = -enemySize + (screenCanvas.width + enemySize * 2) * j;
					p.y = screenCanvas.height / 2;

					//エネミーを新規にセット
					enemy[i].set(p, enemySize, j);

					//一体出現させたのでloopを抜ける
					break;
				}
			}
		}else if(counter === 1000){
			//1000フレーム目にボス出現
			p.x = screenCanvas.width / 2;
			p.y = -80;
			boss.set(p, 50, 30);

			//同時にビットも出現させる
			for(i=0; i<BOSS_BIT_COUNT; i++){
				j = 360 / BOSS_BIT_COUNT;
				bit[i].set(boss, 15, 5, i*j);
			}
		}

		//カウンターの値によってシーン分岐
		switch(true){
			//カウンターが70より小さい
			case counter<70:
				message = 'READY...';
				break;

			//カウンターが100より小さい
			case counter<100:
				message = 'GO!';
				break;

			//カウンターが100以上
			default:
				message = "";

			ctx.beginPath();

			for(i =0; i<ENEMY_MAX_COUNT; i++){
				if(enemy[i].alive){
					enemy[i].move();

					ctx.arc(enemy[i].position.x, enemy[i].position.y, enemy[i].size, 0, Math.PI*2, false);

					//ショットを打つかどうかのパラメータの値からチェック
					if(enemy[i].param % 30 === 0){
						//エネミーショットを調査する
						for(j=0; j<ENEMY_SHOT_MAX_COUNT; j++){
							if(!enemyShot[j].alive){
								//エネミーショットを新規にセットする
								p = enemy[i].position.distance(chara.position);
								p.normalize();
								enemyShot[j].set(enemy[i].position, p, 5, 5);

								//一個出現させたのでループを抜ける
								break;
							}
						}
					}

					ctx.closePath();
				}
			}

			ctx.fillStyle = ENEMY_COLOR;

			ctx.fill();

			ctx.beginPath();

			for(i=0; i<ENEMY_MAX_COUNT; i++){
				if(enemyShot[i].alive){
					enemyShot[i].move();

					ctx.arc(
						enemyShot[i].position.x,
						enemyShot[i].position.y,
						enemyShot[i].size,
						0, Math.PI*2, false
					);

					ctx.closePath();
				}
			}

			ctx.fillStyle = ENEMY_SHOT_COLOR;

			ctx.fill();

			//ボス---------------------------------------
			//パスの設定を開始
			ctx.beginPath();

			//ボスの出現フラグをチェック
			if(boss.alive){
				//ボスを動かす
				boss.move();

				//ボスを描くパスを設定
				ctx.arc(
					boss.position.x,
					boss.position.y,
					boss.size,
					0, Math.PI*2, false
				);

				//パスをいったん閉じる
				ctx.closePath();
			}

			//ボスの色設定
			ctx.fillStyle = BOSS_COLOR;

			//ボスを描く
			ctx.fill();

			//ビット-------------------------------------
			//パスの設定開始
			ctx.beginPath();

			//全てのビットを調査する
			for(i=0; i<BOSS_BIT_COUNT; i++){
				//ビットの出現フラグをチェック
				if(bit[i].alive){
					// ビットを動かす
					bit[i].move();

					//ビットを描くパスを設定
					ctx.arc(
						bit[i].position.x,
						bit[i].position.y,
						bit[i].size,
						0, Math.PI*2, false
					);

					//ショットを打つかどうかパラメータの値からチェック
					if(bit[i].param %25 === 0){
						//エネミーショットを調査する
						for(j=0; j<ENEMY_SHOT_MAX_COUNT; j++){
							if(!enemyShot[j].alive){
								//エネミーショットを新規にセットする
								p = bit[i].position.distance(chara.position);
								p.normalize();
								enemyShot[j].set(bit[i].position, p, 4, 1.5);

								//一個出現させたのでループを抜ける
								break;
							}	
						}
					}

					//パスをいったん閉じる
					ctx.closePath();
				}
			}
			

			//ビットの色を指定する
			ctx.fillStyle = BOSS_BIT_COLOR;

			//ビットを描く
			ctx.fill();
			

			//衝突判定----------------------------------------------
			//全ての自機ショットを調査する
			for(i=0; i<CHARA_SHOT_MAX_COUNT; i++){
				//自機ショットの生存フラグをチェック
				if(charaShot[i].alive){
					//自機ショットとエネミーとの衝突判定
					for(j=0; j<ENEMY_MAX_COUNT; j++){
						//エネミーの生存フラグをチェック
						if(enemy[j].alive){
							//エネミーと自機ショットとの距離を計測
							p = enemy[j].position.distance(charaShot[i].position);
							if(p.length() < enemy[j].size){
								//衝突したら生存フラグを下ろす
								enemy[j].alive = false;
								charaShot[i].alive = false;

								//スコア加算のためのインクリメント
								score++;

								//衝突があったらループを抜ける
								break;
							}
						}
					}

					//自機ショットとボスビットとの衝突判定
					for(j=0; j<BOSS_BIT_COUNT; j++){
						//ビットの生存フラグをチェック
						if(bit[j].alive){
							//ビットと自機ショットとの距離を計測
							p = bit[j].position.distance(charaShot[i].position);
							if(p.length() < bit[j].size){
								//衝突していたら耐久値をデクリメント
								bit[j].life--;

								//自機そっとの生存フラグを下ろす
								charaShot[i].alive = false;

								//耐久値がマイナスになったら生存フラグを下ろす
								if(bit[j].life < 0){
									bit[j].alive = false;
									score += 3;
								}

								//衝突があったらループを抜ける
								break;
							}
						}
					}

					//ボスの生存フラグをチェック
					if(boss.alive){
						//自機ショットとボスとの衝突判定
						p = boss.position.distance(charaShot[i].position);
						if(p.length() < boss.size){
							//衝突していたら耐久値をデクリメントする
							boss.life--;

							//自機ショットの生存フラグを下ろす
							charaShot[i].alive = false;

							//耐久値がマイナスになったらクリア
							if(boss.life < 0){
								score += 10;
								run = false;
								message = 'Clear!';
							}
						}
					}
				}
			}

			//自機とエネミーショットとの衝突判定
			for(i=0; i<ENEMY_SHOT_MAX_COUNT; i++){
				//エネミーショットの生存フラグをチェック
				if(enemyShot[i].alive){
					//自機とエネミーショットとの距離を計測
					p = chara.position.distance(enemyShot[i].position);
					if(p.length()<chara.size){
						//衝突していたら生存フラグを下ろす
						chara.alive = false;

						//衝突があったのでパラメーターを変更してループを抜ける
						run = false;
						message = 'GAME OVER';
						break;
					}
				}
			}
			break;
	}

	//HTMLの更新
	info.innerHTML = 'SCORE: ' + (score*100) + ' ' + message;

	//フラグにより再帰呼び出し
	if(run){setTimeout(arguments.callee, fps);}
	})();
};

// event --------------------------
function mouseMove(event){
	//マウスカーソル座標の更新
	mouse.x = event.clientX - screenCanvas.offsetLeft;
	mouse.y = event.clientY - screenCanvas.offsetTop;
}

function keyDown(event){
	//キーコードを取得
	var ck = event.keyCode;

	//Escキーが押されていたらフラグを下ろす
	if(ck === 27){run = false;}
}

function mouseDown(event){
	//フラグを立てる
	fire = true;
}
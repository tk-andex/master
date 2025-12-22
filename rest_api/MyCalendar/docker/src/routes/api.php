<?php

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Route;
use App\Http\Controllers\KintoneController;
use App\Http\Controllers\UserController;

/*
|--------------------------------------------------------------------------
| API Routes
|--------------------------------------------------------------------------
|
| Here is where you can register API routes for your application. These
| routes are loaded by the RouteServiceProvider and all of them will
| be assigned to the "api" middleware group. Make something great!
|
*/

Route::get('/user', function (Request $request) {
    return $request->user();
});

Route::get('/kintone/records', [KintoneController::class, 'index']);
// Route::get('/kintone/records', [KintoneController::class, 'create']);
Route::get('/user', [UserController::class, 'index']);
Route::post('/kintone/records', [KintoneController::class, 'store']);
Route::post('/user', [UserController::class, 'store']);

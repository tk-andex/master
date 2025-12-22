<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\UserController;

use App\Http\Controllers\KintoneController;

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider and all of them will
| be assigned to the "web" middleware group. Make something great!
|
*/

Route::get('/', function () {
    return view('welcome');
});

Route::get('/employee/{userId}', [KintoneController::class, 'showEmployee']);
Route::get('/users', [UserController::class, 'index'])->name('users.index');
Route::get('/user', [UserController::class, 'showPage']);
Route::post('/users/sync', [UserController::class, 'syncApi'])->name('users.sync');
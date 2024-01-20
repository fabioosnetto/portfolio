import { NgModule } from '@angular/core';
import { PreloadAllModules, PreloadingStrategy, RouterModule, Routes } from '@angular/router';

const routes: Routes = [
  {
    path: '', pathMatch: 'full', redirectTo: 'users-list'
  },

  {
    path: 'users-list',
    loadChildren: () => import('../user/users-list/users-list.module').then(m => m.UsersListModule)
  },

  {
    path: 'user-register',
    loadChildren: () => import('../user/user-register/user-register.module').then(m => m.UserRegisterModule)
  },

  {
    path: 'user-edit/:id',
    loadChildren: () => import('../user/user-register/user-register.module').then(m => m.UserRegisterModule)
  },

  {
    path: '**', pathMatch: 'full', redirectTo: 'users-list'
  },
];

@NgModule({
  imports: [RouterModule.forRoot(routes, {
    preloadingStrategy: PreloadAllModules
  })],
  exports: [RouterModule]
})
export class AppRoutingModule { }

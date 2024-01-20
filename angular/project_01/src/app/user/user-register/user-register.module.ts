import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';

import { UserRegisterRoutingModule } from './user-register-routing.module';
import { UserRegisterComponent } from './component/user-register.component';
import { UserService } from '../user.service';


@NgModule({
  declarations: [UserRegisterComponent],
  imports: [
    CommonModule,
    FormsModule,
    ReactiveFormsModule,
    UserRegisterRoutingModule,
  ],
  providers: [UserService]
})
export class UserRegisterModule { }

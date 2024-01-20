import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { UsersListComponent } from './component/users-list.component';
import { UsersListRoutingModule } from './users-list-routing.module';
import { UserService } from '../user.service';



@NgModule({
  declarations: [UsersListComponent],
  imports: [
    CommonModule,
    UsersListRoutingModule
  ],
  providers: [UserService]
})
export class UsersListModule { }

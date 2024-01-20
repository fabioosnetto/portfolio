import { Component, OnInit } from '@angular/core';
import { User } from '../../User';
import { UserService } from '../../user.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-users-list',
  templateUrl: './users-list.component.html',
  styleUrl: './users-list.component.css'
})
export class UsersListComponent implements OnInit {
  private _users: User[] | null = [];

  private _loadingPage: boolean = false;
  private _noResult:    boolean = false;

  constructor(
    private _userService: UserService,
    private _router: Router
  ) {}

  async ngOnInit(): Promise<void> {
    this.loadPage();
  }

  public get users(): User[] | null { return this._users; }
  public get loadingPage(): boolean { return this._loadingPage; }
  public get noResult(): boolean { return this._noResult; }


  public async loadPage(): Promise<void> {
    this._loadingPage = true;

    this._users = await this.getUsers();

    if(!this.users) this._noResult = true;
    this._loadingPage = false;
  }

  //--- Get Users
  public async getUsers(): Promise<User[] | null> {
    try {
      const resp: User[] = (await this._userService.getUsers()).map(u => new User(u));
      return resp.length ? resp : null;
      
    } catch (err) {
      console.error(err);
      return null;
    }
  }

  // See User
  seeUser(id: number) {
    this._router.navigateByUrl(`user-edit/${id}`)
  }
}
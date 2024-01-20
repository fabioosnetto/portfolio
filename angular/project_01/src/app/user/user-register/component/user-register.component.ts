import { Component, OnDestroy, OnInit } from '@angular/core';
import { FormBuilder, FormControl, FormGroup, Validators } from '@angular/forms';
import { UserService } from '../../user.service';
import { User, UserDTO } from '../../User';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-user-register',
  templateUrl: './user-register.component.html',
  styleUrls: ['./user-register.component.css'] // Note the correct property name
})
export class UserRegisterComponent implements OnInit, OnDestroy {

  private _pageTitle: string = '';
  private _user: User | null = new User();

  private _userForm: FormGroup;
  private _loadingPage: boolean = false;
  private _noResult:    boolean = false;

  constructor(
    private _formBuilder: FormBuilder,
    private _userService: UserService,
    private _route: ActivatedRoute
  ) {
    this._userForm = _formBuilder.group({
      username:  new FormControl(null, Validators.required),
      firstName: new FormControl(null, Validators.required),
      lastName:  new FormControl(null, Validators.required),
      city:      new FormControl(null, Validators.required),
      state:     new FormControl(null, Validators.required),
      status:    new FormControl('1', Validators.required),
    });
  }

  async ngOnInit(): Promise<void> {
    this._pageTitle = this.isEditing ? 'Edit User' : 'Register User';
    await this.loadPage();
  }
  ngOnDestroy(): void {
  }


  public get pageTitle(): string { return this._pageTitle; }
  public get user(): User | null { return this._user; }
  public get userForm(): FormGroup { return this._userForm; }
  public get loadingPage(): boolean { return this._loadingPage; }
  public get noResult(): boolean { return this._noResult; }

  //--- Load Page
  public async loadPage(): Promise<void> {
    try {
      this._loadingPage = true;
      if(!this.isEditing) return;

      const userID: number | null = this.getUserIDFromRoute;
      if(!userID) throw new Error('An invalid user ID was providen.')

      this._user = await this.getUserByID(userID);
      if(!this._user) throw new Error('The requested user was not found.')

      this.setUserOnUserForm = this._user;

    } catch (err) {
      console.error(err);
      this._noResult = true;
    } finally {
      this._loadingPage = false;
    }
  }

  // Is Editing
  public get isEditing(): boolean {
    const id = this._route.snapshot.paramMap.get('id');
    return id !== null;
  }

  // Get User ID From Route
  public get getUserIDFromRoute(): number | null {
    const id = Number(this._route.snapshot.paramMap.get('id'));
    return isNaN(id) ? null : id;
  }

  // Get User By ID
  public async getUserByID(id: number): Promise<User | null> {
    try {
      const resp: User = new User(await this._userService.getUserByID(id));
      return resp ? resp : null;

    } catch (err) {
      return null;
    }
  }

  // Fill User to User Form
  public set setUserOnUserForm(user: User) {
    this._userForm.setValue({
      username:  user.username,
      firstName: user.firstName,
      lastName:  user.lastName,
      city:      user.city,
      state:     user.state,
      status:    user.status,
    });
  }

  // On Form Change
  public onFormChange(): void {
    if(!this._user) return;
    this._user.username  = this._userForm.get('username')?.value;
    this._user.firstName = this._userForm.get('firstName')?.value;
    this._user.lastName  = this._userForm.get('lastName')?.value;
    this._user.city      = this._userForm.get('city')?.value;
    this._user.state     = this._userForm.get('state')?.value;
    this._user.status    = this._userForm.get('status')?.value;
  }

  //--- Save User
  public async saveUser(): Promise<boolean> {
    if(this._userForm.invalid || !this._user) return false;
    this._loadingPage = true;

    try {
      const resp: User = new User(await this._userService.saveUser(this._user.getUserDTO));

      this._userForm.reset(null);
      this._loadingPage = false;
      return true;

    } catch (err) {
      console.error(err);
      this._loadingPage = false;
      return false;
    }
  }
  

  //--- Delete User
  public async deleteUser(): Promise<boolean> {
    try {
      if(this._userForm.invalid || !this._user?.id) return false;
      this._loadingPage = true;

      const resp: void = await this._userService.deleteUser(this._user.id);

      this._userForm.reset(null);
      return true;

    } catch (err) {
      console.error(err);
      return false;

    } finally {
      this._loadingPage = false;
    }
  }
}
